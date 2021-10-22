from typing import Any, Dict, List

from library.types.exceptions import CircularDependsOn


def tree_depth(tree: Dict[str, Any]) -> int:
    """
    Walk through a dependency tree ( with or without level information )
    and return the deepest dependency chain

    Recursively calls itself until tree.depends-on is empty for every branch,
    adds 1 to every call it made, and propagates up the max depth per level
    """
    return max(
        [tree_depth(depends) + 1 for depends in tree["depends-on"] if depends] or [0]
    )


def dependency_tree(
    service: str,
    services: Dict[str, Any],
    parents: List[str] = [],
) -> Dict[str, Any]:
    """
    Given some service name, build a dependency tree for it

    `depends-on` is a recursive list of dependency trees
    for every service that the root service depends on

    `level` notates how many services deep the deepest
    depeonds-on chain goes, where 0 means no dependencies

    {
        "name": "service-name",
        "level": <int>,
        "depends-on": [{...}, ...]
    }
    """
    if service in (parents or []):
        CircularDependsOn(service, parents or []).exit()

    parents = [*parents, service]
    dependencies = services[service].get("depends-on", [])
    no_level = {
        "name": service,
        "depends-on": [dependency_tree(it, services, parents) for it in dependencies],
    }

    return {**no_level, "level": tree_depth(no_level)}


def flat_tree(tree):
    """
    Given a dependency tree, flatten it and remove depends-on information

    If services are created in the order of service.order,
    explicit dependency information shouldn't matter
    """
    return [{"name": tree["name"], "level": tree["level"]}] + [
        item
        for flattened in [flat_tree(it) for it in tree["depends-on"]]
        for item in flattened
    ]


# TODO belongs in a pretty printing part of the code
def render_tree(tree: Dict[str, Any], level: int = 0) -> str:
    depends: list[Any] = tree.get("depends-on", [])

    return f"\n{'  '*level} | ".join(
        [tree["name"], *(render_tree(it, level + 1) for it in depends)]
    )
