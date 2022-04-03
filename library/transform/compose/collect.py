from typing import Dict, List, Set

from library import resolve


# TODO librarian
def namespace(space: str, name: str):
    if not space:
        return name

    return ".".join((space, name))


def trace(name: str = "", parents: Set = set()):
    if not (imports := resolve.get(name).get("import", [])):
        return

    if name:
        imports = [namespace(name, import_name) for import_name in imports]

    for import_name in imports:
        if import_name in parents:
            raise ValueError(parents.union(import_name))  # TODO better type

        trace(import_name, parents.union(name))


def collect_single(name: str = "") -> Dict:
    compose = resolve.get(name)
    imports = [
        namespace(name, import_name) for import_name in compose.get("import", [])
    ]

    return {
        **collect(imports),
        **{
            namespace(name, key): service
            for key, service in compose.get("service", {}).items()
        },
    }


def collect(names: List[str] = [""]) -> Dict:
    return {
        name: service
        for import_name in names
        for name, service in collect_single(import_name).items()
    }
