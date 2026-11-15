"""Tiny sample library used to exercise the AI Software Factory."""
import re

_SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def is_slug(text: str) -> bool:
    """True if text is lowercase ascii alphanumerics joined by single hyphens."""
    return _SLUG.fullmatch(text) is not None


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
