from typing import Dict, List

import pytest

from library import terraform, value
from library.model.command import CommandKind

cases = [
    [
        CommandKind.init,
        {},
        {},
        [value.TERRAFORM_EXECUTABLE, "init"],
    ],
    [
        CommandKind.up,
        {},
        {},
        [value.TERRAFORM_EXECUTABLE, "apply", "-auto-approve"],
    ],
    [
        CommandKind.down,
        {"chdir": "/tf-compose"},
        {"no-color": True, "state": "/state"},
        [
            value.TERRAFORM_EXECUTABLE,
            "-chdir",
            "/tf-compose",
            "apply",
            "-auto-approve",
            "-destroy",
            "-no-color",
            "true",
            "-state",
            "/state",
        ],
    ],
]


@pytest.mark.parametrize("command,terraform_opts,service_opts,want", cases)
def test_build_command(
    command: CommandKind,
    terraform_opts: Dict,
    service_opts: Dict,
    want: List[str],
):
    assert terraform.build_command(command, terraform_opts, service_opts) == want
