from typing import Any, Dict, List

from library.transform import tree


def order_levels(trees: List[Dict[str, Any]]) -> List[List[str]]:
    """
    Given a collection of dependency trees,
    walk down them and collect services at the same level

    The collection returned are groups of services
    that may be brought up at the same time, in appropriate order
    """
    services_flat = [
        service
        for flattened in [tree.flat_tree(it) for it in trees]
        for service in flattened
    ]

    if not services_flat:
        return []

    ordered = [set() for _ in range(max(it["level"] for it in services_flat) + 1)]

    for service in services_flat:
        ordered[service["level"]].add(service["name"])

    return [*filter(bool, map(list, ordered))]


def order_flat(trees: List[Dict[str, Any]]) -> List[str]:
    return [service for group in order_levels(trees) for service in group]
