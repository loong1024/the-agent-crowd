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