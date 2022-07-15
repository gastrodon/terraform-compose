from typing import Dict, List

import pytest

from library import value
from library.execute import command
from library.model.command import CommandKind

cases = [
    [
        "/tf-compose",
        CommandKind.init,
        {},
        {},
        [
            [
                value.TERRAFORM_EXECUTABLE,
                "-chdir",
                "/tf-compose",
                "init",
            ],
        ],
    ],
    [
        "/tf-compose",
        CommandKind.up,
        {},
        {},
        [
            [
                value.TERRAFORM_EXECUTABLE,
                "-chdir",
                "/tf-compose",
                "plan",
                "-out",
                value.TERRAFORM_PLAN_FILE,
            ],
            [
                value.TERRAFORM_EXECUTABLE,
                "-chdir",
                "/tf-compose",
                "apply",
                value.TERRAFORM_PLAN_FILE,
                "-auto-approve",
            ],
        ],
    ],
    [
        "/tf-compose",
        CommandKind.down,
        {},
        {"no-color": True, "state": "/state"},
        [
            [
                value.TERRAFORM_EXECUTABLE,
                "-chdir",
                "/tf-compose",
                "plan",
                "-destroy",
                "-out",
                value.TERRAFORM_PLAN_FILE,
                "-no-color",
                "true",
                "-state",
                "/state",
            ],
            [
                value.TERRAFORM_EXECUTABLE,
                "-chdir",
                "/tf-compose",
                "apply",
                value.TERRAFORM_PLAN_FILE,
                "-auto-approve",
                "-no-color",
                "true",
                "-state",
                "/state",
            ],
        ],
    ],
]


@pytest.mark.parametrize("path,command_kind,terraform_opts,service_opts,want", cases)
def test_build_command(
    path: str,
    command_kind: CommandKind,
    terraform_opts: Dict,
    service_opts: Dict,
    want: List[str],
):
    assert (
        command.build_command(path, command_kind, terraform_opts, service_opts) == want
    )
