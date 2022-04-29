from typing import Any


def merge(source: Any, include: Any, lists=True) -> Any:
    if isinstance(source, set) and lists:
        return source.union(include)

    if isinstance(source, (list, tuple)) and lists:
        return source + include

    if isinstance(source, dict):
        return {
            **include,
            **{
                key: merge(value, include[key], lists=lists)
                if key in include
                else value
                for key, value in source.items()
            },
        }

    return include
