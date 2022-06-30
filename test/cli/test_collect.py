from typing import Dict, List

import pytest

from library import cli
from library.model.cli import ArgumentScope
from library.model.cli.argument import Argument, ArgumentFlag, ArgumentKV

cases = [
    [
        [
            ArgumentKV("hello", "world", ArgumentScope.terraform),
        ],
        None,
        {"hello": "world"},
    ],
    [
        [
            ArgumentFlag("online", ArgumentScope.terraform),
        ],
        None,
        {"online": True},
    ],
    [
        [
            ArgumentFlag("foo", ArgumentScope.terraform),
            ArgumentFlag("bar", ArgumentScope.compose),
        ],
        ArgumentScope.compose,
        {"bar": True},
    ],
]


@pytest.mark.parametrize("arguments,scope,want", cases)
def test_collect(arguments: List[Argument], scope: ArgumentScope, want: Dict):
    assert cli.collect(arguments, scope) == want
