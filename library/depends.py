from typing import Any, Dict, List, Optional, Set

from library.types.exceptions import CircularDependsOn

TAB: str = "\t"


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
        "depends_on": [{...}, ...]
    }
    """
    if service in (parents or []):
        CircularDependsOn(service, parents or []).exit()

    depends_on = services[service].get("depends_on", [])

    return {
        "name": service,
        "depends_on": [
            tree(
                it,
                services,
                [*parents, service],
            )
            for it in depends_on
        ],
    }


def order(services: Dict[str, Any]) -> List[str]:
    ...


def render(tree: Dict[str, Any], level: int = 0) -> str:
    depends: list[Any] = tree.get("depends_on", [])

    return f"\n{'  '*level} | ".join(
        [tree["name"], *(render(it, level + 1) for it in depends)]
    )
