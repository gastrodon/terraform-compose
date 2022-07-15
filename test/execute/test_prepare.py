from typing import Dict, List

import pytest

from library import value
from library.execute import prepare
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


@pytest.mark.parametrize("path,command,terraform_opts,service_opts,want", cases)
def test_build_command(
    path: str,
    command: CommandKind,
    terraform_opts: Dict,
    service_opts: Dict,
    want: List[str],
):
    assert prepare.build_command(path, command, terraform_opts, service_opts) == want
