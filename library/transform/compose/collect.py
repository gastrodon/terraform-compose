from typing import Dict, List, Set

from library import resolve


# TODO librarian
def namespace(space: str, name: str):
    if not space:
        return name

    return ".".join((space, name))


def trace_imports(name: str = "", parents: Set = set()):
    if not (imports := resolve.get(name).get("import", [])):
        return

    if name:
        imports = [namespace(name, import_name) for import_name in imports]

    for import_name in imports:
        if import_name in parents:
            raise ValueError(parents.union(import_name))  # TODO better type

        trace_imports(import_name, parents.union(name))


def collect_import(name: str = "") -> Dict:
    compose = resolve.get(name)
    imports = [
        namespace(name, import_name) for import_name in compose.get("import", [])
    ]

    return {
        **collect_imports(imports),
        **{
            namespace(name, key): service
            for key, service in compose.get("services", {}).items()
        },
    }


def collect_imports(names: List[str] = [""]) -> Dict:
    return {
        name: service
        for import_name in names
        for name, service in collect_import(import_name).items()
    }
