from typing import Any, List, Tuple, TypeVar, Union

FlatPath = List[Union[str, int]]
FlatItem = TypeVar("FlatItem", int, float, str, None)
FlatDict = List[Tuple[FlatPath, FlatItem]]


def flatten(source: Any, path=[]) -> List[Tuple[FlatPath, FlatItem]]:
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
