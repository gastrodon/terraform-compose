from typing import Dict

from library import transform
from library.load.route import handle
from library.transform import compose as transform_compose


@handle
def trace_imports(command: ..., args: ..., compose: Dict):
    transform.trace()
    return compose


@handle
def load_imports(command: ..., args: ..., compose: Dict):
    return {**compose, "services": transform.collect()}


@handle
def include_global(command: ..., args: ..., compose: Dict):
    return compose  # TODO

    return {
        **compose,
        **{
            service: transform_compose.merge(descriptor, compose["globals"])
            for descriptor in compose["services"]
        },
    }


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
