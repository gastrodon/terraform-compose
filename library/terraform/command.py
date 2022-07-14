from typing import Any, Dict, List

from library import value
from library.model.command import CommandKind


def serialize_argument(field: str, value: Any) -> List[str]:
    dashed = f"-{field}"

    if isinstance(value, bool):
        return [dashed, str(value).lower()]

    if isinstance(value, list):
        return [token for sub in value for token in [dashed, sub]]

    if isinstance(value, dict):
        return [token for key, sub in value.items for token in [dashed, f"{key}={sub}"]]

    return [dashed, value]

def serialize_every_argument(opts: Dict) -> List[any]:
    return [
        token
        for field, value in opts.items()
        for token in serialize_argument(field, value)
    ]


def serialize_command(command: CommandKind) -> List[List[str]]:
    match command:
        case CommandKind.up:
            return ["apply", "-auto-approve"]
        case CommandKind.down:
            return ["apply", "-auto-approve", "-destroy"]
        case _:
            return [command.name]


def build_plan_apply(command: CommandKind, terraform_opts: Dict, service_opts: Dict) -> List[List[str]]:
    ...


def build_command(
    command: CommandKind, terraform_opts: Dict, service_opts: Dict
) -> List[List[str]]:
    if command == CommandKind.up or command == CommandKind.down:
        return build_plan_apply(command, terraform_opts, service_opts)

    return [
        [
            value.TERRAFORM_EXECUTABLE,
            *serialize_every_argument(terraform_opts),
            *serialize_command(command),
            *serialize_every_argument(service_opts),
        ]
    ]
