from typing import Any, Dict, List


def resolve(source: Dict, path: List) -> Any:
    """
    Given a source dictionary and a path, return the resolved value

    Returns the source dictionary if path is empty,
    and throws a KeyError if we can't resolve to a value
    """
    if not path:
        return source

    return resolve(source[path[0]], path[1:])
