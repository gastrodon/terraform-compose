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
        ["-file", "compose.yml"],
        [
            ArgumentKV("file", "compose.yml", ArgumentScope.terraform),
        ],
    ],
    [
        ["-context", "./foo/compose", "-context", "./bar/compose"],
        [
            ArgumentKV("context", "./foo/compose", ArgumentScope.terraform),
            ArgumentKV("context", "./bar/compose", ArgumentScope.terraform),
        ],
    ],
    [
        ["--"],
        [
            ArgumentSeparator(),
        ],
    ],
    [
        ["-context", "/root", "--", "service.foo.path", "./bingus"],
        [
            ArgumentKV("context", "/root", ArgumentScope.terraform),
            ArgumentSeparator(),
            ArgumentKV("service.foo.path", "./bingus", ArgumentScope.compose),
        ],
    ],
    [
        ["up", "-var-file", "./var"],
        [
            ArgumentCommand("up"),
            ArgumentKV("var-file", ["./var"], ArgumentScope.command),
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
            ArgumentKV("var-file", ["./vars"], ArgumentScope.command),
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
    [
        ["up", "-var-file", "./foobar", "-var-file", "./baz"],
        [
            ArgumentCommand("up"),
            ArgumentKV("var-file", ["./foobar", "./baz"], ArgumentScope.command),
        ],
    ],
]


@pytest.mark.parametrize("tokens,want", cases)
def test_arguments(tokens: List[str], want: List[Argument]):
    assert cli.arguments(tokens) == cli.sort(want)
