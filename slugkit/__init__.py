"""Tiny sample library used to exercise the AI Software Factory."""


def slugify(text: str, *, max_length: int | None = None) -> str:
    """Lowercase text and join alphanumeric words with single hyphens.

    If max_length is set, truncate to at most that many chars, never ending in a hyphen.
    """
    out, word = [], []
    for ch in text.lower():
        if ch.isascii() and ch.isalnum():
            word.append(ch)
        elif word:
            out.append("".join(word))
            word = []
    if word:
        out.append("".join(word))
    slug = "-".join(out)
    if max_length is not None:
        slug = slug[: max(max_length, 0)].rstrip("-")
    return slug
