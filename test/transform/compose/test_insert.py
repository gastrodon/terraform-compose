from typing import Any, Dict, List

import pytest

from library.transform import compose

cases = [
    [
        {},
        {},
        None,
        {},
    ],
    [
        {"hello": "world"},
        {},
        None,
        {"hello": "world"},
    ],
    [
        {},
        ["hello"],
        "world",
        {"hello": "world"},
    ],
    [
        {},
        ["hello", "tiny"],
        "world",
        {"hello": {"tiny": "world"}},
    ],
    [
        {"hello": {"large": "world"}},
        ["hello", "tiny"],
        "world",
        {"hello": {"tiny": "world", "large": "world"}},
    ],
    [
        {"hello": {"large": "world"}},
        ["hello", "large"],
        "sun",
        {"hello": {"large": "sun"}},
    ],
]


@pytest.mark.parametrize("source,path,value,want", cases)
def test_insert(source: Dict, path: List, value: Any, want: Dict):
    assert compose.insert(source, path, value) == want
