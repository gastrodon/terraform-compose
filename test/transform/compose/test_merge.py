from typing import Dict

import pytest

from library.transform import compose

cases = [
    [
        {"hello": "world"},
        {"world": "hello"},
        {"hello": "world", "world": "hello"},
    ],
    [
        {"hello"},
        {"world"},
        {"hello", "world"},
    ],
    [
        {"hello"},
        {"world", "hello"},
        {"hello", "world"},
    ],
    [
        {"hello": "there"},
        {"hello": "world"},
        {"hello": "world"},
    ],
    [
        {"hello": ["there"]},
        {"hello": ["world"]},
        {"hello": ["there", "world"]},
    ],
    [
        {"hello": {"there"}},
        {"hello": {"world"}},
        {"hello": {"there", "world"}},
    ],
    [
        {"head": {"child": {"another"}}},
        {"head": {"parent": {"yet some other"}}},
        {"head": {"child": {"another"}, "parent": {"yet some other"}}},
    ],
    [
        {"very": {"very": {"very": "nested"}}},
        {"very": {"very": {"also": "important"}}},
        {"very": {"very": {"very": "nested", "also": "important"}}},
    ],
]


@pytest.mark.parametrize("source,include,want", cases)
def test_merge(source: Dict, include: Dict, want: Dict):
    assert compose.merge(source, include) == want
