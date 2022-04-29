from typing import Any, List

from library.model.flat import FlatEntries


def flatten(source: Any, path=[]) -> List[FlatEntries]:
    if isinstance(source, dict):
        return [
            (flat_key, flat_value)
            for key, value in source.items()
            for flat_key, flat_value in flatten(value, path + [key])
        ]

    if isinstance(source, (list, set, tuple)):
        return [
            (flat_key, flat_value)
            for index, value in enumerate(source)
            for flat_key, flat_value in flatten(value, path + [index])
        ]

    return [(path, source)]
