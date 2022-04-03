from typing import Dict

import pytest

from library.resolve import resolve
from library.transform.compose import collect

cases = [
    {
        "": {"import": ["hello"]},
        "hello": {"import": ["world"]},
        "hello.world": {},
    }
]

cases_no_compose = [{"": {"import": ["hello"]}}]


@pytest.mark.parametrize("resolution", cases)
def test_trace(resolution: Dict):
    resolve.set(resolution)

    try:
        collect.trace()

    except ValueError as err:
        assert False, err


@pytest.mark.parametrize("resolution", cases_no_compose)
def test_trace_no_compose(resolution: Dict):
    resolve.set(resolution)

    try:
        collect.trace()
        assert False, resolution

    except KeyError as err:
        return
