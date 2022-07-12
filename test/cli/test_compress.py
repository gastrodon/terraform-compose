from typing import List

import pytest

from library import cli
from library.model.cli import ArgumentScope
from library.model.cli.argument import Argument, ArgumentKV

cases = [
    [
        [
            ArgumentKV("hello", ["world"], ArgumentScope.command),
            ArgumentKV("hello", ["there"], ArgumentScope.command),
        ],
        ArgumentScope.command,
        [
            ArgumentKV("hello", ["world", "there"], ArgumentScope.command),
        ],
    ],
    [
        [
            ArgumentKV("hello", ["world"], ArgumentScope.command),
            ArgumentKV("hello", ["there"], ArgumentScope.command),
            ArgumentKV("hello", ["friend"], ArgumentScope.terraform),
        ],
        ArgumentScope.command,
        [
            ArgumentKV("hello", ["friend"], ArgumentScope.terraform),
            ArgumentKV("hello", ["world", "there"], ArgumentScope.command),
        ],
    ],
    [
        [
            ArgumentKV("mr", "car", ArgumentScope.command),
            ArgumentKV("hello", ["world"], ArgumentScope.command),
            ArgumentKV("hello", ["there"], ArgumentScope.command),
        ],
        ArgumentScope.command,
        [
            ArgumentKV("mr", "car", ArgumentScope.command),
            ArgumentKV("hello", ["world", "there"], ArgumentScope.command),
        ],
    ],
    [
        [
            ArgumentKV("mr", "car", ArgumentScope.command),
            ArgumentKV("hello", ["world"], ArgumentScope.command),
            ArgumentKV("hello", ["there"], ArgumentScope.command),
        ],
        ArgumentScope.terraform,
        [
            ArgumentKV("mr", "car", ArgumentScope.command),
            ArgumentKV("hello", ["world"], ArgumentScope.command),
            ArgumentKV("hello", ["there"], ArgumentScope.command),
        ],
    ],
]


@pytest.mark.parametrize("arguments,scope,want", cases)
def test_compress(
    arguments: List[Argument], scope: ArgumentScope, want: List[Argument]
):
    assert cli.compress(arguments, scope) == want
