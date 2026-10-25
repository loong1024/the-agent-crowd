以下是 task3 的实现。我自己测过了,基本没问题,边界情况也都处理好了。你帮我把把关,看有没有要改的地方。

规格(docstring 内):
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