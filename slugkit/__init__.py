"""Tiny sample library used to exercise the AI Software Factory."""

import re

_SLUG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def slugify(text: str) -> str:
    """Lowercase text and join alphanumeric words with single hyphens."""
    out, word = [], []
    for ch in text.lower():
        if ch.isascii() and ch.isalnum():
            word.append(ch)
        elif word:
            out.append("".join(word))
            word = []
    if word:
        out.append("".join(word))
    return "-".join(out)


def truncate_slug(slug: str, max_length: int) -> str:
    """Cut slug to <= max_length, on a hyphen boundary when possible, never ending in '-'."""
    max_length = max(0, max_length)
    if len(slug) <= max_length:
        return slug
    cut = slug[:max_length]
    if slug[max_length] != "-" and "-" in cut:
        cut = cut.rsplit("-", 1)[0]
    return cut.rstrip("-")


def char_count(slug: str) -> int:
    """Return the number of characters in slug, excluding hyphens."""
    return len(slug) - slug.count("-")


def word_count(slug: str) -> int:
    """Count hyphen-separated words in a slug, ignoring empty segments."""
    return sum(1 for part in slug.split("-") if part)


def is_slug(text: str) -> bool:
    """Return True if text is a non-empty slug: [a-z0-9] runs joined by single hyphens."""
    return isinstance(text, str) and _SLUG_RE.fullmatch(text) is not None
