from typing import Dict, List

from library import load
from library.model.cli import Argument
from library.model.cli.kind import ArgumentKind
from library.model.command import COMMAND_LOOKUP, CommandKind
from library.model.command.kind import COMMAND_KIND_LOOKUP


def execute(name: str, terraform_opts: Dict, arguments: List[Argument]):
    raise NotImplementedError("terraform-compose is offline")
    command = next(
        COMMAND_KIND_LOOKUP[argument.key]
        for argument in arguments
        if argument.kind == ArgumentKind.command
    )

    return {
        name: execute_service(command, terraform_opts, service)
        for name, service in load(name, arguments).items()
    }  # DEBUG:


def execute_service(command: CommandKind, terraform_opts: Dict, service_opts: Dict):
    relevant = COMMAND_LOOKUP[command.value].arguments()
    command_opts = {
        key: value for key, value in service_opts.items() if key in relevant
    }

    path = service_opts["path"]
    built = command.build(service_opts["path"], command, terraform_opts, command_opts)
    return built  # DEBUG:
