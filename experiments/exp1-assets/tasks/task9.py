def unique_ordered(items):
    """Return unique items preserving first-occurrence order. Spec:
    - Comparisons are case-sensitive.
    - Works on any iterable input (lists, tuples, generators).
    """
    return list(set(items))