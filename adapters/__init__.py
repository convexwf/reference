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


_ADAPTERS = {
    "ai_agent_book": Adapter("ai_agent_book", "1"),
    "easy_rl": Adapter("easy_rl", "1"),
}


def get_adapter(identifier: str) -> Adapter:
    """Return a known adapter or raise an actionable error."""

    try:
        return _ADAPTERS[identifier]
    except KeyError as exc:
        known = ", ".join(sorted(_ADAPTERS))
        raise ValueError(f"unknown adapter {identifier!r}; known adapters: {known}") from exc
