from typing import Dict

import pytest

from library.model.dependency import DependsNode
from library.transform import tree

cases = [
    [
        "root",
        {"root": {"depends-on": ["root"]}},
        "root -> root",
    ],
]


@pytest.mark.parametrize("name,services,want", cases)
def test_build_raise(name: str, services: Dict, want: DependsNode):
    try:
        tree.build(name, services)
        assert False, "didn't throw!"

    except ValueError as err:
        assert str(err) == want
