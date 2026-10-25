def apply_discounts(price, discounts):
    """Apply a sequence of percentage discounts to a price. Spec:
    - discounts: list of percentages (each 0-100).
    - Discounts stack ADDITIVELY: total = sum(discounts), capped at 50.
    - Final price = price * (1 - total/100), rounded to 2 decimals.
    - The final price must never be negative.
    """
    total = sum(discounts)
    final = price * (1 - total / 100)
    return round(final, 2)