from __future__ import annotations

import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from tools.reference_core import (
    ReferenceError,
    SourceSnapshot,
    assert_document_contract,
    build_document,
    manifest_from_data,
    rewrite_link_target,
    validate_manifest_sources,
)
from tools.source_cache import _sparse_patterns


COMMIT = "0123456789abcdef0123456789abcdef01234567"


def manifest_data() -> dict:
    return {
        "id": "fixture-book",
        "title": "测试合集",
        "source": {"repository": "https://github.com/example/fixture-book.git", "ref": "main"},
        "language": "zh-CN",
        "adapter": "ai_agent_book",
        "output": "markdown/fixture-book/complete.md",
        "front_matter": {
            "authors": ["测试作者"],
            "tags": ["fixture", "tutorial"]
        },
        "sections": [
            {
                "title": "正文",
                "parts": [
                    {"path": "docs/first.md", "title": "第一章"},
                    {"path": "docs/next.md", "title": "第二章"},
                ],
            }
        ],
        "completeness": {"required_globs": ["docs/*.md"]},
    }


class ReferenceCoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "docs").mkdir()
        (self.root / "images").mkdir()
        (self.root / "images" / "演示 图.png").write_bytes(b"fixture")
        (self.root / "articles").mkdir()
        (self.root / "articles" / "lesson.md").write_text(
            "<!DOCTYPE html><html><body><div class=\"book-post\">"
            "<h1>00 HTML 课程</h1><p>正文 <strong>重点</strong>，"
            "<a href=\"../evidence/data.md\">资料</a>。</p>"
            "<h3>跳过的源标题层级</h3>"
            "<p><img src=\"../images/diagram.png?wh=100\" alt=\"流程图 [详情]\"></p>"
            "<ul><li>第一项</li><li>第二项</li></ul>"
            "<pre><code class=\"language-python\">print('ok')</code></pre>"
            "</div></body></html>",
            encoding="utf-8",
        )
        (self.root / "docs" / "first.md").write_text(
            "# 原始标题\n\n"
            "<div align=\"center\">\n"
            "<img src=\"../images/演示 图.png\" alt=\"示例图\">\n"
            "</div>\n\n"
            "![另一张图](../images/演示%20图.png){width=60%}\n\n"
            "[下一章](next.md#more)\n\n"
            "![官方图](https://raw.githubusercontent.com/example/fixture-book/main/images/演示%20图.png)\n\n"
            "[官方下一章](https://github.com/example/fixture-book/blob/main/docs/next.md#more)\n\n"
            "[未检出证据](../evidence/data.json#result)\n\n"
            "[未检出目录](../evidence)\n\n"
            "<p class=\"caption\"><strong>图注</strong>与<em>强调</em></p>\n\n"
            "## 小节\n",
            encoding="utf-8",
        )
        (self.root / "docs" / "next.md").write_text("# 第二章\n\n## 更多\n", encoding="utf-8")
        self.manifest = manifest_from_data(manifest_data())
        self.snapshot = SourceSnapshot(
            self.manifest,
            self.root,
            COMMIT,
            "2026-09-14T00:00:00+00:00",
            "2024-01-01",
            "2026-09-14",
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_build_rewrites_images_links_and_html(self) -> None:
        document = build_document(self.snapshot)
        raw = f"https://raw.githubusercontent.com/example/fixture-book/{COMMIT}/images/%E6%BC%94%E7%A4%BA%20%E5%9B%BE.png"
        self.assertEqual(document.count(raw), 3)
        self.assertIn(f"https://github.com/example/fixture-book/blob/{COMMIT}/docs/next.md#more", document)
        self.assertIn("### 第一章", document)
        self.assertIn("#### 小节", document)
        self.assertIn('  - "测试作者"', document)
        self.assertIn('published_at: "2024-01-01"', document)
        self.assertNotIn("source_repository:", document)
        self.assertNotIn("<img", document)
        self.assertNotIn("align=", document)
        self.assertNotIn("{width=60%}", document)
        self.assertIn("**图注**与*强调*", document)
        self.assertNotIn("<strong", document)
        self.assertNotIn("<p", document)

    def test_build_rewrites_entries_not_materialized_in_sparse_checkout(self) -> None:
        sparse_snapshot = replace(
            self.snapshot,
            repository_entries={
                "docs/first.md": "blob",
                "docs/next.md": "blob",
                "images/演示 图.png": "blob",
                "evidence": "tree",
                "evidence/data.json": "blob",
            },
        )
        document = build_document(sparse_snapshot)
        base = f"https://github.com/example/fixture-book/blob/{COMMIT}"
        self.assertIn(f"{base}/evidence/data.json#result", document)
        self.assertIn(f"https://github.com/example/fixture-book/tree/{COMMIT}/evidence", document)

    def test_build_recovers_unique_asset_from_legacy_relative_path(self) -> None:
        source = self.root / "docs" / "first.md"
        source.write_text(
            source.read_text(encoding="utf-8")
            + "\n![迁移后的图片](../legacy-copy/assets/%E6%BC%94%E7%A4%BA%20%E5%9B%BE.png)\n",
            encoding="utf-8",
        )
        sparse_snapshot = replace(
            self.snapshot,
            repository_entries={
                "docs/first.md": "blob",
                "docs/next.md": "blob",
                "images/演示 图.png": "blob",
            },
        )
        document = build_document(sparse_snapshot)
        raw = f"https://raw.githubusercontent.com/example/fixture-book/{COMMIT}/images/%E6%BC%94%E7%A4%BA%20%E5%9B%BE.png"
        self.assertEqual(document.count(raw), 4)

    def test_preserves_malformed_third_party_url(self) -> None:
        target = "https://github.com/ethereum/wiki/blob/master/[中文]-權益證明機制FAQ.md"
        self.assertEqual(rewrite_link_target(target, self.root / "docs" / "first.md", self.snapshot), target)

    def test_sparse_checkout_contains_only_listed_parts(self) -> None:
        self.assertEqual(_sparse_patterns(("docs/first.md", "docs/next.md")), ["/docs/first.md", "/docs/next.md"])

    def test_html_article_profile_selects_sources_and_converts_content(self) -> None:
        data = manifest_data()
        data.pop("adapter")
        data["render"] = {"source_format": "html_article", "article_class": "book-post"}
        data["sections"] = [
            {
                "title": "正文",
                "selection": {
                    "include_globs": ["articles/*.md"],
                    "exclude_paths": ["articles/promo.md"],
                },
            }
        ]
        data["completeness"] = {"required_globs": ["articles/*.md"]}
        manifest = manifest_from_data(data)
        snapshot = SourceSnapshot(
            manifest,
            self.root,
            COMMIT,
            "2026-09-14T00:00:00+00:00",
            "2024-01-01",
            "2026-09-14",
            {
                "articles": "tree",
                "articles/lesson.md": "blob",
                "articles/promo.md": "blob",
                "images": "tree",
                "images/diagram.png?wh=100": "blob",
                "evidence": "tree",
                "evidence/data.md": "blob",
            },
        )
        document = build_document(snapshot)
        raw = f"https://raw.githubusercontent.com/example/fixture-book/{COMMIT}/images/diagram.png%3Fwh=100"
        self.assertIn("### lesson", document)
        self.assertIn("#### 跳过的源标题层级", document)
        self.assertIn("正文 **重点**，[资料]", document)
        self.assertIn(raw, document)
        self.assertIn("![流程图 \\[详情\\]]", document)
        self.assertIn(f"https://github.com/example/fixture-book/blob/{COMMIT}/evidence/data.md", document)
        self.assertIn("- 第一项", document)
        self.assertIn("```python\nprint('ok')\n```", document)
        self.assertNotIn("<!DOCTYPE", document)
        self.assertNotIn("<div", document)

    def test_completeness_ignores_nested_archive_copy(self) -> None:
        tree_snapshot = replace(
            self.snapshot,
            repository_entries={
                "docs/first.md": "blob",
                "docs/next.md": "blob",
                "archive/review/docs/omitted.md": "blob",
            },
        )
        validate_manifest_sources(tree_snapshot)

    def test_completeness_rejects_new_unlisted_source(self) -> None:
        (self.root / "docs" / "omitted.md").write_text("# 未收录", encoding="utf-8")
        with self.assertRaisesRegex(ReferenceError, "omitted from manifest"):
            validate_manifest_sources(self.snapshot)

    def test_contract_rejects_local_image(self) -> None:
        with self.assertRaisesRegex(ReferenceError, "local image target"):
            assert_document_contract("# 文档\n\n![本地](images/local.png)\n")


if __name__ == "__main__":
    unittest.main()
