import functools
from typing import Dict, List

from library.cli.collect import collect
from library.model.cli import Argument, ArgumentKind, ArgumentScope
from library.transform import compose


def interpolate(services: Dict, arguments: List[Argument]) -> Dict:
    mergeable = collect(arguments, ArgumentScope.command)

    merged = {
        name: compose.merge(descriptor, mergeable)
        for name, descriptor in services.items()
    }

    insertions = [
        (argument.key.split("."), argument.value)
        for argument in arguments
        if argument.scope == ArgumentScope.compose
        and argument.kind != ArgumentKind.separator
    ]

    return functools.reduce(
        lambda last, insertion: compose.insert(last, insertion[0], insertion[1]),
        [merged, *insertions],
    )
