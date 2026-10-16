"""Whitespace normalization for TextKit."""


def normalize_whitespace(text: str) -> str:
    """Return *text* with surrounding whitespace removed and every run of
    Unicode whitespace collapsed to a single ASCII space.

    Empty or whitespace-only input yields an empty string. Punctuation and
    letter case are preserved unchanged.
    """
    return " ".join(text.split())
