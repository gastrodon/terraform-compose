from typing import Any, Dict, List

import pytest

from library.transform import compose

cases = [
    [
        {},
        [],
        {},
    ],
    [
        420_69,
        [],
        420_69,
    ],
    [
        {"hello": "world"},
        ["hello"],
        "world",
    ],
    [
        {"stinky": ["huge", "ed award", "picks e", "a lice"]},
        ["stinky", 0],
        "huge",
    ],
    [
        {"service": {"foo": {"path": "nowhere"}}},
        ["service", "foo"],
        {"path": "nowhere"},
    ],
]


@pytest.mark.parametrize("source,path,want", cases)
def test_resolve(source: Dict, path: List[str], want: Any):
    assert compose.resolve(source, path) == want
