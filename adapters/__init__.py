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
    robust_fences: bool = False
    normalize_space_before_tabs: bool = False


_ADAPTERS = {
    "generic": Adapter("generic", "1"),
    "ai_agent_book": Adapter("ai_agent_book", "1"),
    "ai_infra_book": Adapter("ai_infra_book", "1"),
    "easy_rl": Adapter("easy_rl", "1"),
    "easy_vibe": Adapter(
        "easy_vibe",
        "4",
        source_h1_titles=True,
        promote_repeated_h1=True,
        strip_vitepress_scaffolding=True,
        robust_fences=True,
    ),
    "whale_quant": Adapter("whale_quant", "1", normalize_space_before_tabs=True),
    "hello_agents": Adapter("hello_agents", "1"),
}


def get_adapter(identifier: str) -> Adapter:
    """Return a known adapter or raise an actionable error."""

    try:
        return _ADAPTERS[identifier]
    except KeyError as exc:
        known = ", ".join(sorted(_ADAPTERS))
        raise ValueError(f"unknown adapter {identifier!r}; known adapters: {known}") from exc
