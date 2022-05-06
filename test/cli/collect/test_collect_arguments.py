from typing import List

import pytest

from library import cli
from library.model.cli.argument import Argument, ArgumentCommand, ArgumentSeparator

cases = [
    [
        ["-hello", "world"],
        [
            Argument("hello", "world"),
        ],
    ],
    [
        ["-hello", "world", "-hello", "again"],
        [
            Argument("hello", "world"),
            Argument("hello", "again"),
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
            Argument("chdir", "/root"),
            ArgumentSeparator(),
            Argument("service.foo.path", "./bingus"),
        ],
    ],
    [
        ["up", "-path", "./path"],
        [
            ArgumentCommand("up"),
            Argument("path", "./path"),
        ],
    ],
]


@pytest.mark.parametrize("tokens,want", cases)
def test_collect_arguments(tokens: List[str], want: List[Argument]):
    collect = cli.collect_arguments(tokens)
    assert collect == want

    for argument in collect:
        if isinstance(argument, ArgumentCommand):
            assert argument.command is not None
