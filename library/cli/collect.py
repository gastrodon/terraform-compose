import functools
from typing import Dict, List, Optional

from library.model.cli import Argument, ArgumentScope
from library.transform import compose


def collect(arguments: List[Argument], scope: Optional[ArgumentScope] = None) -> Dict:
    return functools.reduce(
        lambda last, insertion: compose.insert(last, insertion[0], insertion[1]),
        [
            {},
            *[
                (argument.key.split("."), argument.value)
                for argument in arguments
                if not scope or argument.scope == scope
            ],
        ],
    )
