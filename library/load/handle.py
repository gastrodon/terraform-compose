from typing import Dict, List

from library import transform
from library.load.route import handle
from library.model.cli import Argument


@handle
def trace_imports(args: List[Argument], compose: Dict):
    transform.trace()
    return compose


@handle
def load_imports(args: List[Argument], compose: Dict):
    return {**compose, "service": transform.collect()}


@handle
def include_global(args: List[Argument], compose: Dict):
    return compose  # TODO

    return {
        **compose,
        **{
            service: transform.compose.merge(descriptor, compose["globals"])
            for descriptor in compose["service"]
        },
    }


@handle
def include_cli(args: List[Argument], compose: Dict):
    return compose  # TODO


@handle
def absolutize_paths(args: List[Argument], compose: Dict):
    return transform.path.absolutize(compose)


@handle
def locate_services(args: List[Argument], compose: Dict):
    return compose  # TODO


@handle
def locate_dependencies(args: List[Argument], compose: Dict):
    return compose  # TODO


@handle
def path_dependencies(args: List[Argument], compose: Dict):
    return compose  # TODO


@handle
def invert(args: List[Argument], compose: Dict):
    return compose  # TODO


@handle
def pluck(args: List[Argument], compose: Dict):
    return compose  # TODO


@handle
def snake_case(args: List[Argument], compose: Dict):
    return compose  # TODO


@handle
def bash_interop(args: List[Argument], compose: Dict):
    return compose  # TODO


@handle
def at_files(args: List[Argument], compose: Dict):
    return compose  # TODO
