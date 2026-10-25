冷审以下实现。
- 你不知道作者是谁,也不要推测作者身份或意图。
- 对照下面的规格(docstring)逐条检查。
- 每条发现必须附代码证据(引用具体代码片段)。
- 结论按 pass / fail / blocked / skipped / unverified 五级给出。
- 只报告有证据的实质问题;不要复述代码,不要客套。

def parse_csv_row(line):
    """Parse a single CSV line into fields. Spec:
    - Handles quoted fields containing commas (RFC-4180 double quotes).
    - A double quote inside a quoted field is escaped by doubling it ("").
    - Returns [] for empty or blank input (whitespace only).
    """
    if line == "":
        return []
    fields = []
    current = ""
    in_quotes = False
    for ch in line:
        if ch == '"':
            in_quotes = not in_quotes
        elif ch == ',' and not in_quotes:
            fields.append(current)
            current = ""
        else:
            current += ch
    fields.append(current)
    return fields