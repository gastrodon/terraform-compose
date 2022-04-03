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


def test_trace():
    for case in cases:
        resolve.set(case)

        try:
            collect.trace_imports()

        except ValueError as err:
            assert False, err


def test_trace_no_compose():
    for case in cases_no_compose:
        resolve.set(case)

        try:
            collect.trace_imports()
            assert False, case

        except KeyError as err:
            continue
