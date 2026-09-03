from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.reference_core import (
    ReferenceError,
    SourceSnapshot,
    assert_document_contract,
    build_document,
    manifest_from_data,
    validate_manifest_sources,
)


COMMIT = "0123456789abcdef0123456789abcdef01234567"


def manifest_data() -> dict:
    return {
        "id": "fixture-book",
        "title": "测试合集",
        "source": {"repository": "https://github.com/example/fixture-book.git", "ref": "main"},
        "language": "zh-CN",
        "adapter": "ai_agent_book",
        "output": "markdown/fixture-book/complete.md",
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
        (self.root / "docs" / "first.md").write_text(
            "# 原始标题\n\n"
            "<div align=\"center\">\n"
            "<img src=\"../images/演示 图.png\" alt=\"示例图\">\n"
            "</div>\n\n"
            "![另一张图](../images/演示%20图.png){width=60%}\n\n"
            "[下一章](next.md#more)\n\n"
            "## 小节\n",
            encoding="utf-8",
        )
        (self.root / "docs" / "next.md").write_text("# 第二章\n\n## 更多\n", encoding="utf-8")
        self.manifest = manifest_from_data(manifest_data())
        self.snapshot = SourceSnapshot(self.manifest, self.root, COMMIT, "2026-09-14T00:00:00+00:00")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_build_rewrites_images_links_and_html(self) -> None:
        document = build_document(self.snapshot)
        raw = f"https://raw.githubusercontent.com/example/fixture-book/{COMMIT}/images/%E6%BC%94%E7%A4%BA%20%E5%9B%BE.png"
        self.assertEqual(document.count(raw), 2)
        self.assertIn(f"https://github.com/example/fixture-book/blob/{COMMIT}/docs/next.md#more", document)
        self.assertIn("### 第一章", document)
        self.assertIn("#### 小节", document)
        self.assertNotIn("<img", document)
        self.assertNotIn("align=", document)
        self.assertNotIn("{width=60%}", document)

    def test_completeness_rejects_new_unlisted_source(self) -> None:
        (self.root / "docs" / "omitted.md").write_text("# 未收录", encoding="utf-8")
        with self.assertRaisesRegex(ReferenceError, "omitted from manifest"):
            validate_manifest_sources(self.snapshot)

    def test_contract_rejects_local_image(self) -> None:
        with self.assertRaisesRegex(ReferenceError, "local image target"):
            assert_document_contract("# 文档\n\n![本地](images/local.png)\n")


if __name__ == "__main__":
    unittest.main()
