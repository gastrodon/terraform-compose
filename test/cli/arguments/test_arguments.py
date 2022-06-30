from typing import List

import pytest

from library import cli
from library.model.cli import ArgumentScope
from library.model.cli.argument import (
    Argument,
    ArgumentCommand,
    ArgumentFlag,
    ArgumentKV,
    ArgumentSeparator,
)

cases = [
    [
        ["-compose", "compose.yml"],
        [
            ArgumentKV("compose", "compose.yml", ArgumentScope.terraform),
        ],
    ],
    [
        ["-compose", "./foo/compose", "-compose", "./bar/compose"],
        [
            ArgumentKV("compose", "./foo/compose", ArgumentScope.terraform),
            ArgumentKV("compose", "./bar/compose", ArgumentScope.terraform),
        ],
    ],
    [
        ["--"],
        [
            ArgumentSeparator(),
        ],
    ],
    [
        ["-compose", "/root", "--", "service.foo.path", "./bingus"],
        [
            ArgumentKV("compose", "/root", ArgumentScope.terraform),
            ArgumentSeparator(),
            ArgumentKV("service.foo.path", "./bingus", ArgumentScope.compose),
        ],
    ],
    [
        ["up", "-var-file", "./var"],
        [
            ArgumentCommand("up"),
            ArgumentKV("var-file", "./var", ArgumentScope.command),
        ],
    ],
    [
        [
            "down",
            "-out",
            "./out",
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
            ArgumentKV("out", "./out", ArgumentScope.command),
            ArgumentKV("var-file", "./vars", ArgumentScope.command),
            ArgumentKV("var", "hello=world", ArgumentScope.command),
            ArgumentSeparator(),
            ArgumentKV("service.foo.vars", "hello: world", ArgumentScope.compose),
        ],
    ],
    [
        ["init", "-reconfigure"],
        [
            ArgumentCommand("init"),
            ArgumentFlag("reconfigure", ArgumentScope.command),
        ],
    ],
]


@pytest.mark.parametrize("tokens,want", cases)
def test_arguments(tokens: List[str], want: List[Argument]):
    assert cli.arguments(tokens) == want
