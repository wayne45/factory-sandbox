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
