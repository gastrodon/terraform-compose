from typing import Dict, List

import pytest

from library import cli
from library.model.cli import ArgumentScope
from library.model.cli.argument import Argument, ArgumentFlag, ArgumentKV

cases = [
    [
        {
            "root": {},
            "child": {"path": "./hello"},
            "sibling": {"foo": "idk"},
        },
        [
            ArgumentKV("foo", "bar", ArgumentScope.command),
        ],
        {
            "root": {"foo": "bar"},
            "child": {"foo": "bar", "path": "./hello"},
            "sibling": {"foo": "bar"},
        },
    ],
    [
        {
            "root": {},
            "child": {"path": "./hello"},
            "sibling": {"foo": "idk"},
        },
        [
            ArgumentKV("foo", "bar", ArgumentScope.command),
            ArgumentFlag("destroy", ArgumentScope.command),
        ],
        {
            "root": {"foo": "bar", "destroy": True},
            "child": {"foo": "bar", "path": "./hello", "destroy": True},
            "sibling": {"foo": "bar", "destroy": True},
        },
    ],
]


@pytest.mark.parametrize("compose,arguments,want", cases)
def test_interpolate(compose: Dict, arguments: List[Argument], want: Dict):
    assert cli.interpolate(compose, arguments) == want