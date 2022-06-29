import functools
from typing import Dict, List, Optional, Any,  Union

from library.transform import compose
from library.model.cli import (
    Argument,
    ArgumentScope,
    ArgumentKind,
)

def serialize(argument: Argument) -> Optional[Union[str, Any]]:
    match argument.kind:
        case ArgumentKind.command | ArgumentKind.separator:
            return None
        case ArgumentKind.kv | ArgumentKind.flag:
            return (argument.key, argument.value)
        case _:
            raise ValueError(f"I don't know what {argument} is!")


def interpolate(services: Dict, arguments: List[Argument]) -> Dict:
    mergeable = {
        key: value
        for key, value in filter(
            bool,
            [
                serialize(argument)
                for argument in arguments
                if argument.scope == ArgumentScope.command
            ],
        )
    }

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
        [merged, *insertions]
    )
