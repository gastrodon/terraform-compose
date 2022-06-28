from typing import Dict, List, Set


def group(services: Dict, supporting: Set[str] = set()) -> List[Set[str]]:
    grouped = {
        name
        for name in set(services.keys()) - supporting
        if not set(services[name]["depends-on"]) - supporting
    }

    if not grouped:
        return []

    return [
        grouped,
        *group(services, grouped.union(supporting)),
    ]
