from typing import Callable, Dict, Set, Tuple

from library.cli import parse
from library.model.cli import ArgumentKind
from library.model.cli.parse import ArgumentParser
from library.model.command.base import Command

kv: Dict[str, Tuple[str, Set[str]]] = {
    "backup": ("kv", {"apply"}),
    "input": ("kv", {"apply", "plan"}),
    "lock-timeout": ("kv", {"apply", "plan"}),
    "lock": ("kv", {"apply", "plan"}),
    "parallelism": ("kv", {"apply", "plan"}),
    "state-out": ("kv", {"apply"}),
    "state": ("kv", {"apply", "plan"}),
}

flag: Dict[str, Tuple[str, Set[str]]] = {
    "detailed_exitcode": ("flag", {"apply", "plan"}),
    "refresh-only": ("flag", {"plan"}),
    "no-color": ("flag", {"apply", "plan"}),
    "compact-warnings": ("flag", {"apply", "plan"}),
    "no-color": ("flag", {"apply", "plan"}),
}

listy: Dict[str, Tuple[str, Set[str]]] = {
    "refresh": ("listy", {"plan"}),
    "target": ("listy", {"plan"}),
    "var-file": ("listy", {"plan"}),
}

dicty: Dict[str, Tuple[str, Set[str]]] = {
    "var": ("dicty", {"plan"}),
}


def make_parser(kind: str, commands: Set[str]) -> Callable[[], ArgumentParser]:
    match kind:
        case "kv":
            return ArgumentParser(ArgumentKind.kv, commands=commands)
        case "flag":
            return ArgumentParser(ArgumentKind.flag, False, commands=commands)
        case "listy":
            return ArgumentParser(ArgumentKind.kv, list(), parser=parse.listy, commands=commands)
        case "dicty":
            return ArgumentParser(ArgumentKind.kv, dict(), parser=parse.dicty, commands=commands)
        case _:
            raise ValueError(f"I don't know what {kind} is!")


class Up(Command):
    name = "up"
    extra = {
        key: make_parser(*value)
        for key, value in {**kv, **flag, **listy, **dicty}.items()
    }


class Down(Up):
    name = "down"
