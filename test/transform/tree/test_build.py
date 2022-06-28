from typing import Dict

import pytest

from library.model.dependency import DependsNode
from library.transform import tree

cases = [
    [
        "root",
        {"root": {"depends-on": []}},
        DependsNode(path=["root"]),
    ],
    [
        "root",
        {
            "root": {"depends-on": ["child"]},
            "child": {"depends-on": []},
        },
        DependsNode(
            path=["root"],
            children=[DependsNode(path=["root", "child"])],
        ),
    ],
    [
        "root",
        {
            "root": {"depends-on": ["child", "sibling"]},
            "sibling": {"depends-on": ["child"]},
            "child": {"depends-on": []},
        },
        DependsNode(
            path=["root"],
            children=[
                DependsNode(path=["root", "child"]),
                DependsNode(
                    path=["root", "sibling"],
                    children=[
                        DependsNode(path=["root", "sibling", "child"]),
                    ],
                ),
            ],
        ),
    ],
]


@pytest.mark.parametrize("name,services,want", cases)
def test_build(name: str, services: Dict, want: DependsNode):
    assert tree.build(name, services) == want
