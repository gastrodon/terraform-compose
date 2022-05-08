from enum import Enum


class ArgumentKind(Enum):
    kv: str = "kv"
    flag: str = "flag"
    command: str = "command"
    separator: str = "separator"
