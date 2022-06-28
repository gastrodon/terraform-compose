from typing import Dict, List, Set

import pytest

from library.transform import tree

cases = [
    [
        {
            "root": {"depends-on": []},
        },
        [
            {"root"},
        ],
    ],
    [
        {
            "root": {"depends-on": ["child"]},
            "child": {"depends-on": []},
            "silo": {"depends-on": []},
        },
        [
            {"child", "silo"},
            {"root"},
        ],
    ],
    [
        {
            "root": {"depends-on": ["child", "neighbor"]},
            "neighbor": {"depends-on": ["child"]},
            "child": {"depends-on": []},
            "silo": {"depends-on": []},
        },
        [
            {"child", "silo"},
            {"neighbor"},
            {"root"},
        ],
    ],
]


@pytest.mark.parametrize("name,services,want", cases)
def test_members(name: str, services: Dict, want: List[Set[str]]):
    assert tree.members(name, services) == want
