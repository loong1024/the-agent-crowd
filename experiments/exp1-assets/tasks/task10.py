def parse_version(version):
    """Parse a version string into a comparable tuple of ints. Spec:
    - "1.2.3" -> (1, 2, 3).
    - Missing minor/patch parts default to 0 ("1.2" -> (1, 2, 0); "2" -> (2, 0, 0)).
    - Parts compare numerically ("1.10" > "1.9").
    """
    parts = version.split(".")
    return tuple(parts)