from unittest import TestCase

from library.config.depends import tools

case_find = [
    {
        "have": {"hello": "world"},
        "key": "^hello$",
        "value": None,
        "use_full_path": False,
        "want": {"hello": "world"},
    },
    {
        "have": {"hello": "world"},
        "key": None,
        "value": "^world$",
        "use_full_path": False,
        "want": {"hello": "world"},
    },
    {
        "have": {"hello": "world", "ignore": "me"},
        "key": "^hello$",
        "value": None,
        "use_full_path": False,
        "want": {"hello": "world"},
    },
    {
        "have": {"hello": "world", "ignore": "me"},
        "key": None,
        "value": "^world$",
        "use_full_path": False,
        "want": {"hello": "world"},
    },
    {
        "have": {"hello": {"small": "world"}},
        "key": "^small$",
        "value": None,
        "use_full_path": False,
        "want": {"hello.small": "world"},
    },
    {
        "have": {"hello": {"small": "world"}},
        "key": None,
        "value": "^world$",
        "use_full_path": False,
        "want": {"hello.small": "world"},
    },
    {
        "have": {"world": {"big": {"name": "jupiter"}, "small": {"name": "pluto"}}},
        "key": r"world\..*\.name",
        "value": None,
        "use_full_path": True,
        "want": {"world.big.name": "jupiter", "world.small.name": "pluto"},
    },
    {
        "have": {"world": {"big": {"name": "jupiter"}, "small": {"name": "pluto"}}},
        "key": None,
        "value": ".*",
        "use_full_path": True,
        "want": {"world.big.name": "jupiter", "world.small.name": "pluto"},
    },
]


class TestFind(TestCase):
    def test_find(self):
        for index, case in enumerate(case_find):
            found = tools.find(
                case["have"],
                key=case["key"],
                value=case["value"],
                use_full_path=case["use_full_path"],
            )

            if found != case["want"]:
                raise AssertionError(f"Case #{index+1} produced {found}")
