def merge(them):
    """
    Given a collection of dictionaries,
    recursively merge them and all of their list values
    """
    if not isinstance(them, list):
        return them

    if len(them) == 0:
        return {}

    if len(them) == 1:
        return them[0]

    if len(them) > 2:
        return merge(
            [
                *them[:-2],
                merge(them[-2:]),
            ]
        )

    first, second = them
    writable = {**second}

    for key, value in first.items():
        conflict = writable.get(key)
        if isinstance(value, dict) and isinstance(conflict, dict):
            writable[key] = merge([value, conflict])

        if isinstance(value, list) and isinstance(conflict, list):
            writable[key] = [*map(merge, value + conflict)]

        else:
            writable[key] = value

    return writable


def flatten(collections):
    """
    Given a List[Union[List, Union[..., Any]]], flatten it into a List[Any]

    Union[..., Any] in this case refers to a recursively nesting structure
    """
    return [
        item
        for sub in collections
        for item in (flatten(sub) if isinstance(sub, list) else [sub])
    ]
