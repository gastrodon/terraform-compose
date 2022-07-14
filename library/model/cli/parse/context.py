from dataclasses import dataclass
from typing import Any, List

from library.model.cli.scope import ArgumentScope


@dataclass
class ParserContext:
    tokens: List[str]
    scope: ArgumentScope
    command: Any
