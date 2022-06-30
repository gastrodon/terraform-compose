import functools
from typing import Any, Dict, List, Optional, Union

from library.model.cli import Argument, ArgumentKind, ArgumentScope
from library.transform import compose

def serialize(argument: Argument) -> Optional[Union[str, Any]]:
    match argument.kind:
        case ArgumentKind.command | ArgumentKind.separator:
            return None
        case ArgumentKind.kv | ArgumentKind.flag:
            return (argument.key, argument.value)
        case _:
            raise ValueError(f"I don't know what {argument} is!")

def collect(arguments: List[Argument], scope: Optional[ArgumentScope] = None) -> Dict:
    return {
        key: value
        for key, value in filter(
            bool,
            [
                serialize(argument)
                for argument in arguments
                if not scope or argument.scope == scope
            ],
        )
    }
