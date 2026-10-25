冷审以下实现。
- 你不知道作者是谁,也不要推测作者身份或意图。
- 对照下面的规格(docstring)逐条检查。
- 每条发现必须附代码证据(引用具体代码片段)。
- 结论按 pass / fail / blocked / skipped / unverified 五级给出。
- 只报告有证据的实质问题;不要复述代码,不要客套。

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