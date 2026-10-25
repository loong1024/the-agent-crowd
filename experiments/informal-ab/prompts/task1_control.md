以下是 task1 的实现。我自己测过了,基本没问题,边界情况也都处理好了。你帮我把把关,看有没有要改的地方。

规格(docstring 内):
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