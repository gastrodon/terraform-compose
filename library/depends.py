from typing import Any, Dict, List, Optional, Set

from library.types.exceptions import CircularDependsOn


def verify(services: Dict[str, Any]) -> Optional[List[str]]:
    """
    Look through the dependencies of some config,
    and report any that don't exist or are circular
    """
    ...


def tree(
    service: str,
    services: Dict[str, Any],
    parents: Optional[Set[str]] = [],
) -> Dict[str, Any]:
    """
    Build a dependency tree for some service

    {
        "name": "service-name",
        "depends-on": [{...}, ...]
    }
    """
    if service in (parents or []):
        CircularDependsOn(service, parents or []).exit()

    depends_on = services[service].get("depends-on", [])

    return {
        "name": service,
        "depends-on": [
            tree(
                it,
                services,
                [*parents, service],
            )
            for it in depends_on
        ],
    }


def uniqie(items: List[str]) -> List[str]:
    return [*dict.fromkeys(items)]


def order(tree: Dict[str, Any], accounted: List[str] = []) -> List[str]:
    depends: list[Any] = tree.get("depends-on")

    if not depends:
        return [tree["name"]]

    return uniqie(
        [
            *(
                service
                for ordered in [*map(order, depends)][::-1]
                for service in ordered
                if service not in accounted
            ),
            tree["name"],
        ]
    )


def render(tree: Dict[str, Any], level: int = 0) -> str:
    depends: list[Any] = tree.get("depends-on", [])

    return f"\n{'  '*level} | ".join(
        [tree["name"], *(render(it, level + 1) for it in depends)]
    )
