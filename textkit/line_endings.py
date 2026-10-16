"""Line-ending normalization for TextKit."""


def normalize_line_endings(text: str) -> str:
    """Return *text* with CRLF and lone CR line endings converted to LF.

    Every other character, including existing LF line feeds, is preserved
    unchanged.
    """
    return text.replace("\r\n", "\n").replace("\r", "\n")
