from typing import Dict, List, Optional, Any,  Union

from library import transform
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
    command_mergeable = {
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

    return {
        name: transform.compose.merge(descriptor, command_mergeable)
        for name, descriptor in services.items()
    }
