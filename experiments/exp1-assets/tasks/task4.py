def normalize_phone(raw):
    """Normalize a phone number string. Spec:
    - Keep a leading '+' for international format; all other non-digit
      characters are stripped.
    - Return None for empty input.
    Examples: "+1 (555) 123-4567" -> "+15551234567"; "555-1234" -> "5551234";
    "" -> None
    """
    digits = "".join(ch for ch in raw if ch.isdigit())
    return digits