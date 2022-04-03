from typing import Dict

import pytest

from library.resolve import resolve
from library.transform.compose import collect

cases = [
    [
        {
            "": {"import": ["hello"]},
            "hello": {"service": {"world": {"path": "./planet/earth"}}},
        },
        {
            "hello.world": {"path": "./planet/earth"},
        },
    ],
]


@pytest.mark.parametrize("resolution,service", cases)
def test_trace(resolution: Dict, service: Dict):
    resolve.set(resolution)

    assert collect.collect() == service
