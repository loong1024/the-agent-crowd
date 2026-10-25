def split_full_name(full_name):
    """Split a full name into (first_name, last_name). Spec:
    - "First Last" -> ("First", "Last").
    - Multi-word last names: everything after the first token is the last
      name ("Vincent van Gogh" -> ("Vincent", "van Gogh")).
    - Empty string -> ("", "").
    """
    parts = full_name.split()
    return (parts[0], parts[-1])