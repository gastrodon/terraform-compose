from typing import List

from library.model.cli import ArgumentScope
from library.model.cli.argument import Argument, ArgumentKV


def compress(arguments: List[Argument], scope: ArgumentScope) -> List[Argument]:
    arg_filter = lambda it: isinstance(it.value, (list, dict)) and it.scope == scope
    compressed = {
        argument.key: [] if isinstance(argument.value, list) else {}
        for argument in filter(arg_filter, arguments)
    }

    for argument in filter(arg_filter, arguments):
        if isinstance(argument.value, list):
            compressed[argument.key] += argument.value
        elif isinstance(argument.value, dict):
            compressed[argument.key] = {**compressed[argument.key], **argument.value}

    return [
        *filter(lambda it: not arg_filter(it), arguments),
        *(ArgumentKV(key, value, scope) for key, value in compressed.items()),
    ]
