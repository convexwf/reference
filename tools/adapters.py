"""Book-specific integration adapters.

Adapters deliberately stay small.  The generic renderer owns the portable
Markdown rules; an adapter only gives a source a stable compatibility version
and a place for an exceptional source-specific rule if one is ever needed.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Adapter:
    """A versioned compatibility contract for one source layout."""

    identifier: str
    version: str
    source_h1_titles: bool = False
    promote_repeated_h1: bool = False
    strip_vitepress_scaffolding: bool = False
    normalize_vitepress_containers: bool = False
    drop_announcement_containers: bool = False
    robust_fences: bool = False
    normalize_inline_fence_at_line_start: bool = False
    replace_missing_images_with_notes: bool = False
    redact_openai_api_keys: bool = False
    normalize_trailing_whitespace: bool = False
    normalize_space_before_tabs_in_fences: bool = False
    drop_empty_headings: bool = False
    normalize_space_before_tabs: bool = False
    asset_overrides: tuple[tuple[str, str, str], ...] = ()
    readme_parent_roots: tuple[tuple[str, str], ...] = ()
    reader_note: str | None = None


_ADAPTERS = {
    "generic": Adapter("generic", "1"),
    "ai_agent_book": Adapter("ai_agent_book", "1"),
    "ai_infra_book": Adapter("ai_infra_book", "1"),
    "easy_rl": Adapter("easy_rl", "1"),
    "hands_on_modern_rl": Adapter(
        "hands_on_modern_rl",
        "4",
        source_h1_titles=True,
        strip_vitepress_scaffolding=True,
        normalize_vitepress_containers=True,
        drop_announcement_containers=True,
        robust_fences=True,
        reader_note=(
            "本文档基于 [Hands-On Modern RL](https://github.com/walkinglabs/hands-on-modern-rl) 的中文课程文档整理并转换格式，"
            "原作由 WalkingLabs 及贡献者维护，采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可；"
            "本改编文档也按 CC BY-NC-SA 4.0 发布。分享或改编时请署名并沿用相同许可，且不得用于商业目的。"
        ),
    ),
    "easy_vibe": Adapter(
        "easy_vibe",
        "4",
        source_h1_titles=True,
        promote_repeated_h1=True,
        strip_vitepress_scaffolding=True,
        robust_fences=True,
    ),
    "llm_cookbook": Adapter(
        "llm_cookbook",
        "2",
        robust_fences=True,
        redact_openai_api_keys=True,
        asset_overrides=(("docs/README.md", "figures/qrcode.jpeg", "figures/qrcode.jpeg"),),
    ),
    "self_llm": Adapter(
        "self_llm",
        "1",
        robust_fences=True,
        normalize_inline_fence_at_line_start=True,
        replace_missing_images_with_notes=True,
        normalize_trailing_whitespace=True,
        drop_empty_headings=True,
        asset_overrides=(
            (
                "examples/数字生命/readme.md",
                "屏幕截图 2025-01-23 010103.png",
                "examples/数字生命/image/readme/1738593252102.png",
            ),
        ),
        readme_parent_roots=(
            ("examples", "示例项目"),
            ("models", ""),
            ("models_amd", "AMD GPU"),
            ("models_ascend", "昇腾 Ascend NPU"),
            ("models_mlx", "Apple M 平台"),
        ),
    ),
    "whale_quant": Adapter("whale_quant", "1", normalize_space_before_tabs=True),
    "hello_agents": Adapter("hello_agents", "1"),
    "google_styleguide": Adapter(
        "google_styleguide",
        "1",
        source_h1_titles=True,
        robust_fences=True,
        reader_note=(
            "本指南为 zh-google-styleguide 社区维护的非官方中文译本，内容据 Google Style Guides 原版翻译并转换为 Markdown；"
            "原指南文本采用 [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) 许可；"
            "原作者、译者及来源信息见各指南前言。"
        ),
    ),
    "software_engineering_at_google": Adapter(
        "software_engineering_at_google",
        "2",
        robust_fences=True,
        normalize_space_before_tabs=True,
        normalize_space_before_tabs_in_fences=True,
        reader_note=(
            "本文档基于 [Software Engineering at Google](https://github.com/qiangmzsx/Software-Engineering-at-Google) 的中英文对照译本整合；"
            "原著作者为 Titus Winters、Tom Manshreck 和 Hyrum Wright，中文译本由 qiangmzsx 及贡献者维护。"
            "上游声明图书内容采用 [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) 许可；"
            "本整合稿按相同许可提供。再使用或改编时请保留原著及译本署名，并遵守署名-相同方式共享条款。"
        ),
    ),
    "google_python_styleguide": Adapter(
        "google_python_styleguide",
        "1",
        source_h1_titles=True,
        robust_fences=True,
        reader_note=(
            "本指南为 zh-google-styleguide 社区维护的非官方中文译本，内容据 Google Style Guides 原版翻译并转换为 Markdown；"
            "原指南文本采用 [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) 许可。"
            "Python 指南的代码源文件另采用 Apache License 2.0，见 [许可证副本](../../licenses/google-python-styleguide-APACHE-2.0.txt)；"
            "原作者、译者及来源信息见指南前言。"
        ),
    ),
    "booknotes": Adapter(
        "booknotes",
        "1",
        source_h1_titles=True,
        robust_fences=True,
        reader_note=(
            "本文件是 Preslav Mihaylov 编写的英文学习笔记，按上游 MIT 许可发布；"
            "许可副本见 [MIT License](../../licenses/booknotes-MIT-LICENSE.txt)。"
        ),
    ),
    "healthart_hubermanlab": Adapter(
        "healthart_hubermanlab",
        "1",
        reader_note=(
            "内容整理自 Health Art 项目的 Huberman Lab 中文解析页，不是 Huberman Lab 官方原稿或逐字稿。"
            "健康信息仅作一般知识素材，不构成个人医疗建议；涉及补剂、药物、筛查或治疗时，"
            "请核对原始节目与研究并咨询合格专业人士。"
        ),
    ),
}


def get_adapter(identifier: str) -> Adapter:
    """Return a known adapter or raise an actionable error."""

    try:
        return _ADAPTERS[identifier]
    except KeyError as exc:
        known = ", ".join(sorted(_ADAPTERS))
        raise ValueError(f"unknown adapter {identifier!r}; known adapters: {known}") from exc
