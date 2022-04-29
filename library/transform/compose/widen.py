from typing import Dict, List, Tuple, Union

from library.model.flat import FlatEntries, FlatItem, FlatPath


def widen_entry(entry: Tuple[FlatPath, FlatItem]) -> Union[Dict, List]:
    path, item = entry

    if not path:
        raise ValueError("can't widen without a path!")

    if path[1:]:
        return {path[0]: widen_entry((path[1:], item))}

    return {path[0]: item}


def widen(entries: FlatEntries) -> Union[Dict, List]:
    # TODO ([path, ...], value) => {"path": {"...": value}}
    top_level = {path[0]: {} for path, _ in entries}

    for path, value in entries:
        if path[1:]:
            top_level[path[0]] = merge(widen())

        top_level[path[0]] += (path[1:], value)

    return {key: widen(value) for key, value in top_level.items()}

    return top_level
