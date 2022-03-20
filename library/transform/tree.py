from typing import Any, Callable, Dict, List

from library.transform import tools
from library.types.error import DependsError


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


def invert(tree, parents=[]):
    if not tree:
        return tree

    if not tree["depends-on"]:
        return {
            "name": tree["name"],
            "level": tree["level"],
            "depends-on": parents,
        }

    return tools.merge(
        [
            invert(
                sub,
                parents=[
                    {
                        "name": tree["name"],
                        "level": tree["level"],
                        "depends-on": parents,
                    }
                ],
            )
            for sub in tree["depends-on"]
        ]
    )


def root_dependency_tree(
    services: Dict[str, Any],
    skip: Callable[[Dict[str, Any]], bool] = lambda it: False,
    inverse: bool = False,
) -> Dict[str, Any]:
    """
    Generate a dependency tree for the entire compose file

    The pretend resource at the root doesn't have level information
    """

    depends = [dependency_tree(it, services, skip=skip) for it in services.keys()]
    do = invert if inverse else lambda it: it

    return {
        "name": "",
        "depends-on": [*filter(bool, map(do, depends))],
    }


def dependency_tree(
    service: str,
    services: Dict[str, Any],
    parents: List[str] = [],
    skip: Callable[[Dict[str, Any]], bool] = lambda it: False,
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
        DependsError(service, parents or []).exit()

    if skip(services[service]):
        return {}

    dependencies = services[service].get("depends-on", [])
    no_level = {
        "name": service,
        "depends-on": [
            dependency_tree(it, services, parents=[*parents, service], skip=skip)
            for it in dependencies
            if not skip(services[it])
        ],
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


def flat_trees(trees):
    """
    Given a collection of trees, flatten them all
    """
    if isinstance(trees, list):
        return [*map(flat_trees, trees)]

    return [flat_tree(trees)]
