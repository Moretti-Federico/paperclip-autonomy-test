"""Host development environment probe for TextKit."""


def host_summary() -> str:
    """Return ``"hostdev-ok"`` as a fixed marker for the host-dev pilot run.

    The function is dependency-free on purpose: it only proves that the
    host execution environment can create, import and test new modules.
    """
    return "hostdev-ok"
