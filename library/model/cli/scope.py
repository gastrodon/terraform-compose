from enum import Enum


class ArgumentScope(Enum):
    terraform: str = "terraform"
    command: str = "command"
    compose: str = "compose"
