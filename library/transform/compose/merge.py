from typing import Any


def merge(source: Any, include: Any) -> Any:
    if isinstance(source, set):
        return source.union(include)

    if isinstance(source, (list, tuple)):
        return source + include

    if isinstance(source, dict):
        return {
            **include,
            **{
                key: merge(value, include[key]) if key in include else value
                for key, value in source.items()
            },
        }

    return include
