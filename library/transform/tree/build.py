from typing import Dict, List

from library.model.dependency import DependsNode


def build(name: str, services: Dict, path: List[str] = []) -> DependsNode:
    if name in path:
        # TODO want to be a ComposeError or something!
        raise ValueError(" -> ".join(path + [name]))

    return DependsNode(
        path=path + [name],
        children=[
            build(child, services, path + [name])
            for child in services[name]["depends-on"]
        ],
    )


def build_lookup(compose: Dict) -> Dict[str, DependsNode]:
    return {name: build(name, compose["services"]) for name in compose.keys()}


def build_lookup_inverse(compose: Dict) -> Dict[str, DependsNode]:
    inverted: Dict = {
        name: {
            "depends-on": [
                sub_name
                for sub_name, service in compose["services"].items()
                if name in service["depends-on"]
            ]
        }
        for name in compose["services"].keys()
    }

    return inverted
