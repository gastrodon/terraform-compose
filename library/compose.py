from typing import Dict, List, Optional, Set

from library.types.exceptions import CircularDependsOn


def dependency_verify(services: Dict[str, any]) -> Optional[List[str]]:
    """
    Look through the dependencies of some config,
    and report any that don't exist or are circular
    """
    ...


def dependency_tree(
    service: str, services: Dict[str, any], parents: Optional[Set[str]] = []
) -> Dict[str, any]:
    """
    Build a dependency tree for some service

    {
        "name": "service-name",
        "depends_on": [{...}, ...]
    }
    """
    if service in (parents or []):
        raise CircularDependsOn(service, parents or [])

    depends_on = services[service].get("depends_on", [])

    return {
        "name": service,
        "depends_on": [
            dependency_tree(
                it,
                services,
                [*parents, service],
            )
            for it in depends_on
        ],
    }


def dependency_order(services: Dict[str, any]) -> List[str]:
    ...
