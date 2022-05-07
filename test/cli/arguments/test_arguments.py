from typing import List

import pytest

from library import cli
from library.model.cli import ArgumentScope
from library.model.cli.argument import Argument, ArgumentCommand, ArgumentSeparator
from library.model.command import CommandKind

cases = [
    [
        ["-hello", "world"],
        [
            Argument("hello", "world", ArgumentScope.terraform),
        ],
    ],
    [
        ["-hello", "world", "-hello", "again"],
        [
            Argument("hello", "world", ArgumentScope.terraform),
            Argument("hello", "again", ArgumentScope.terraform),
        ],
    ],
    [
        ["--"],
        [
            ArgumentSeparator(),
        ],
    ],
    [
        ["-chdir", "/root", "--", "service.foo.path", "./bingus"],
        [
            Argument("chdir", "/root", ArgumentScope.terraform),
            ArgumentSeparator(),
            Argument("service.foo.path", "./bingus", ArgumentScope.compose),
        ],
    ],
    [
        ["up", "-path", "./path"],
        [
            ArgumentCommand("up"),
            Argument("path", "./path", ArgumentScope.command.value(CommandKind.up)),
        ],
    ],
    [
        [
            "down",
            "-path",
            "./path",
            "-var-file",
            "./vars",
            "-var",
            "hello=world",
            "--",
            "service.foo.vars",
            "hello: world",
        ],
        [
            ArgumentCommand("down"),
            Argument("path", "./path", ArgumentScope.command.value(CommandKind.down)),
            Argument(
                "var-file", "./vars", ArgumentScope.command.value(CommandKind.down)
            ),
            Argument(
                "var", "hello=world", ArgumentScope.command.value(CommandKind.down)
            ),
            ArgumentSeparator(),
            Argument("service.foo.vars", "hello: world", ArgumentScope.compose),
        ],
    ],
]


@pytest.mark.parametrize("tokens,want", cases)
def test_collect_arguments(tokens: List[str], want: List[Argument]):
    collect = cli.arguments(tokens)
    assert collect == want

    for argument in collect:
        if isinstance(argument, ArgumentCommand):
            assert argument.command is not None
