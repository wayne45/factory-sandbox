"""Tiny sample library used to exercise the AI Software Factory."""


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


def shout(slug: str) -> str:
    """Return slug in upper case."""
    return slug.upper()


def starts_with_digit(slug: str) -> bool:
    """Return True if slug is non-empty and starts with an ASCII digit (0-9)."""
    return bool(slug) and slug[0] in "0123456789"


def ends_with_digit(slug: str) -> bool:
    """Return True if slug is non-empty and ends with an ASCII digit (0-9)."""
    return bool(slug) and slug[-1] in "0123456789"


def is_all_digits(s: str) -> bool:
    """Return True if s is non-empty and every character is an ASCII digit (0-9)."""
    return bool(s) and all(ch in "0123456789" for ch in s)
