from typing import Dict, List

import pytest

from library.transform import compose

cases = [
    [
        {},
        {},
        [],
    ],
    [
        {"hello": "world"},
        {"key": r"^hello$"},
        [["hello"]],
    ],
    [
        {"foo": "uwu", "bar": "uwu"},
        {"value": "uwu"},
        [["foo"], ["bar"]],
    ],
    [
        {
            "service": {
                "foo": {"backend": "./dev", "path": "./foo/"},
                "bar": {"path": "./", "var": {"hello": "world"}},
            }
        },
        {"value": r"\.\/.*/?"},
        [
            ["service", "foo", "backend"],
            ["service", "foo", "path"],
            ["service", "bar", "path"],
        ],
    ],
    [
        {
            "service": {
                "hello": {"path": ".", "var": {}},
                "world": {"path": ".", "backend": "/tmp/rary"},
            }
        },
        {"key": r"service\..+\.path"},
        [
            ["service", "hello", "path"],
            ["service", "world", "path"],
        ],
    ],
    [
        {
            "service": {
                "hello": {"path": ".", "var": {}},
                "world": {"path": ".", "backend": "/tmp/rary"},
            }
        },
        {"key": r"service-.+-path", "separator": "-"},
        [
            ["service", "hello", "path"],
            ["service", "world", "path"],
        ],
    ],
]


@pytest.mark.parametrize("source,kwargs,want", cases)
def test_find_key(source: Dict, kwargs: Dict, want: List[str]):
    assert compose.find(source, **kwargs) == want
