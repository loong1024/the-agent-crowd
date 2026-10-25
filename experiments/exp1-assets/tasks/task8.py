def format_duration(seconds):
    """Format a duration in seconds as "Xh Ym Zs". Spec:
    - Zero units are omitted ("3600" -> "1h"; "65" -> "1m 5s").
    - If everything is zero, return "0s".
    - Negative input raises ValueError.
    """
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    parts = []
    if h:
        parts.append(f"{h}h")
    if m:
        parts.append(f"{m}m")
    parts.append(f"{s}s")
    return " ".join(parts)