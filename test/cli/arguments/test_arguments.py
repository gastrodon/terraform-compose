from typing import List

import pytest

from library import cli
from library.model.cli import ArgumentScope
from library.model.cli.argument import ArgumentCommand, ArgumentKV, ArgumentSeparator

cases = [
    [
        ["-chdir", "world"],
        [
            ArgumentKV("chdir", "world", ArgumentScope.terraform),
        ],
    ],
    [
        ["-chdir", "world", "-chdir", "again"],
        [
            ArgumentKV("chdir", "world", ArgumentScope.terraform),
            ArgumentKV("chdir", "again", ArgumentScope.terraform),
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
            ArgumentKV("chdir", "/root", ArgumentScope.terraform),
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
]


@pytest.mark.parametrize("tokens,want", cases)
def test_collect_arguments(tokens: List[str], want: List[ArgumentKV]):
    collect = cli.arguments(tokens)
    assert collect == want
