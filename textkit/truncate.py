"""Text truncation for TextKit."""


def truncate(text: str, width: int) -> str:
    """Return *text* shortened so the result fits within *width*.

    Text no longer than *width* is returned unchanged. Longer text is
    cut so the result has length exactly *width*; when *width* is at
    least three the cut is ``text[:width - 3] + "..."``, while smaller
    widths keep a hard cut. Non-positive *width* yields an empty string.
    """
    if width <= 0:
        return ""
    if len(text) <= width:
        return text
    if width < 3:
        return text[:width]
    return text[:width - 3] + "..."
