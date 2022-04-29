from typing import Any, Dict, List

from library.transform.compose import merge


def widen(path: List, value: Any) -> Any:
    """
    Given a path and a value, widen it into a value
    """

    if not path:
        return value

    if isinstance(path[0], int):
        return [widen(path[1:], value)]

    return {path[0]: widen(path[1:], value)}


def insert(source: Dict, path: List, value: Any) -> Dict:
    """
    Given a source dict, path and insertion value, return a mutated source
    in which the value is inserted at its path location
    """
    if not path:
        return source

    return merge.merge(source, widen(path, value))
