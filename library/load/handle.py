from typing import Dict

from library.load.route import handle


@handle
def imports(command: ..., args: ..., compose: Dict):
    if not compose.get("import", []):
        return compose  # TODO

    raise NotImplementedError("import isn't implemented")


@handle
def include_global(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def include_cli(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def locate_services(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def locate_dependencies(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def path_dependencies(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def invert(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def pluck(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def snake_case(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def bash_interop(command: ..., args: ..., compose: Dict):
    return compose  # TODO


@handle
def at_files(command: ..., args: ..., compose: Dict):
    return compose  # TODO
