from dataclasses import dataclass
from typing import List

from library.model.cli.scope import ArgumentScope
from library.model.command import CommandKind


@dataclass
class ParseContext:
    tokens: List[str]
    scope: ArgumentScope
    command: CommandKind
