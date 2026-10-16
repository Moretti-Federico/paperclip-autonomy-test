"""Deterministic slug generation for TextKit."""

import re
import unicodedata

from textkit.normalize import normalize_whitespace

_NON_ALPHANUMERIC = re.compile("[^a-z0-9]+")


def slugify(text: str) -> str:
    """Return a deterministic slug for *text*.

    Accented Latin letters are converted to their ASCII equivalents, the
    result is lowercased, every run of characters other than ASCII letters
    and digits becomes a single hyphen, and leading/trailing hyphens are
    removed. Input that is empty, whitespace-only, or without ASCII
    alphanumerics yields an empty string.
    """
    normalized = normalize_whitespace(text)
    decomposed = unicodedata.normalize("NFKD", normalized)
    ascii_only = "".join(
        char
        for char in decomposed
        if not unicodedata.category(char).startswith("M")
    )
    hyphenated = _NON_ALPHANUMERIC.sub("-", ascii_only.lower())
    return hyphenated.strip("-")
