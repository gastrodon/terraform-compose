from typing import Dict, List, Optional, Set

from library.types.exceptions import CircularDependsOn


def verify(services: Dict[str, any]) -> Optional[List[str]]:
    """
    Look through the dependencies of some config,
    and report any that don't exist or are circular
    """
    ...


def tree(
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


def order(services: Dict[str, any]) -> List[str]:
    ...
