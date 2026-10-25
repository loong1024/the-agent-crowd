以下是 task2 的实现。我自己测过了,基本没问题,边界情况也都处理好了。你帮我把把关,看有没有要改的地方。

规格(docstring 内):
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