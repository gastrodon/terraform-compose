from typing import Any, Dict, List

from library import value
from library.model.command import CommandKind, Up
from library.model.command import COMMAND_LOOKUP


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


def build_plan_apply(
    path: str,
    command: CommandKind,
    terraform_opts: Dict,
    command_opts: Dict
) -> List[List[str]]:
    parsers = Up.arguments()
    plan_opts = {
        key: value
        for key, value in command_opts.items()
        if "plan" in parsers[key].commands
    }

    apply_opts = {
        key: value
        for key, value in command_opts.items()
        if"apply" in parsers[key].commands
    }

    return [
        [
            value.TERRAFORM_EXECUTABLE,
            "-chdir",
            path,
            *serialize_every_argument(terraform_opts),
            *(["plan", "-destroy"] if command == CommandKind.down else ["plan"]),
            "-out",
            value.TERRAFORM_PLAN_FILE,
            *serialize_every_argument(plan_opts),
        ],
        [
            value.TERRAFORM_EXECUTABLE,
            "-chdir",
            path,
            *serialize_every_argument(terraform_opts),
            "apply",
            value.TERRAFORM_PLAN_FILE,
            "-auto-approve",
            *serialize_every_argument(apply_opts),
        ],
    ]


def build_command(
    path: str,
    command: CommandKind,
    terraform_opts: Dict,
    command_opts: Dict
) -> List[List[str]]:
    if command == CommandKind.up or command == CommandKind.down:
        return build_plan_apply(path, command, terraform_opts, command_opts)

    return [
        [
            value.TERRAFORM_EXECUTABLE,
            "-chdir",
            path,
            *serialize_every_argument(terraform_opts),
            *serialize_command(command),
            *serialize_every_argument(command_opts),
        ]
    ]
