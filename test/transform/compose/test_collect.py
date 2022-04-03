from typing import Dict

import pytest

from library.resolve import resolve
from library.transform.compose import collect

cases = [
    [
        {
            "": {"import": ["hello"]},
            "hello": {"services": {"world": {"path": "./planet/earth"}}},
        },
        {
            "hello.world": {"path": "./planet/earth"},
        },
    ],
]


@pytest.mark.parametrize("resolution,services", cases)
def test_trace(resolution: Dict, services: Dict):
    resolve.set(resolution)

    assert collect.collect() == services
