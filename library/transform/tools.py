import re

from library.transform import flat, tools


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


def find(collection, key: str = None, value: str = None, use_full_path=False):
    """
    Given a Union[List[Dict], Dict], recursively iterate values
    and return values that are like key, value, or both
    in the form of { path: value }
    """
    if key is None and value is None:
        raise Warning("key and value are None, nothing to find!")

    key_re = re.compile(key) if key is not None else None
    value_re = re.compile(value) if value is not None else None

    found = {}
    for key, value in flat.flatten_map(collection).items():
        if key_re:
            if key_re.match(key) and use_full_path:
                found[key] = value

            elif key_re.match(key.split(".")[-1]):
                found[key] = value

        if isinstance(value, (float, int)):
            value = str(value)

        if not value_re or not isinstance(value, str):
            continue

        if value_re.match(value):
            found[key] = value

    return found


def pluck(service, tree):
    """
    Given a dependency tree, pluck a service out of it
    """
    if tree["name"] == service:
        return tree

    return tools.merge(
        tools.flatten(
            filter(
                bool,
                (pluck(service, it) for it in tree["depends-on"]),
            )
        )
    )
