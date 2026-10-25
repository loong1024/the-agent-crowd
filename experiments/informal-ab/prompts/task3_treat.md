冷审以下实现。
- 你不知道作者是谁,也不要推测作者身份或意图。
- 对照下面的规格(docstring)逐条检查。
- 每条发现必须附代码证据(引用具体代码片段)。
- 结论按 pass / fail / blocked / skipped / unverified 五级给出。
- 只报告有证据的实质问题;不要复述代码,不要客套。

def add_tag(tags=[], new_tag=""):
    """Add new_tag to a tags list, returning the updated list. Spec:
    - Called without tags: starts from an empty list.
    - The input list must NOT be mutated.
    - Order preserved; duplicate tags ignored.
    """
    if new_tag == "":
        return tags
    tags.append(new_tag)
    return list(set(tags))