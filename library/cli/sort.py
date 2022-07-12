from typing import List

from library.model.cli import Argument


def get_key(argument: Argument) -> str:
    return f"{argument.scope}_{argument.key}"


def sort(arguments: List[Argument]) -> List[Argument]:
    return sorted(arguments, key=get_key)
