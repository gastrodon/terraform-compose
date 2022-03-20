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


def flatten_map(collection, prefix: str = ""):
    """
    Given a Dict[str, Any], flatten it into a Dict[str, T]
    where T is anything that isn't a dict,
    and all of the keys are at the root level in dot notation
    """
    flat = {}
    namespaced = {
        ".".join((prefix, key)) if prefix else key: value
        for key, value in collection.items()
    }

    for key, value in namespaced.items():
        if isinstance(value, dict):
            flat = {**flat, **flatten_map(value, prefix=key)}
            continue

        flat[key] = value

    return flat
