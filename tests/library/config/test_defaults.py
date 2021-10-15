from typing import Any, Dict, List
from unittest import TestCase

from library.config.defaults import Item


class TestItemValidateAgainst(TestCase):
    """
    Test Item.validate_against
    """

    def test_int(self):
        assert Item.validate_against(42096, int)
        assert Item.validate_against(-1, int)
        assert not Item.validate_against("1", int)

    def test_str(self):
        assert Item.validate_against("foobar", str)

    def test_bool(self):
        assert Item.validate_against(True, bool)
        assert Item.validate_against(False, bool)

    def test_list_int(self):
        assert Item.validate_against([1, 2, 3], List[int])
        assert not Item.validate_against([1, 2, 3], List[str])
        assert not Item.validate_against([1, "2", 3], List[str])

    def test_dict_str_int(self):
        assert Item.validate_against({"1": 1, "foo": 2}, Dict[str, int])
        assert not Item.validate_against({1: 1, "foo": 2}, Dict[str, int])
        assert not Item.validate_against({"1": 1, "foo": "bar"}, Dict[str, int])
        assert not Item.validate_against({"1": 1, "foo": 2}, Dict[int, int])

    def test_nested(self):
        assert Item.validate_against(
            {"foo": {1: [1, 2]}},
            Dict[str, Dict[int, List[int]]],
        )

        assert not Item.validate_against(
            {"foo": {1: [1, "2"]}},
            Dict[str, Dict[int, List[int]]],
        )

        assert not Item.validate_against(
            {"foo": {"1": [1, "2"]}},
            Dict[str, Dict[int, List[int]]],
        )

        assert not Item.validate_against(
            {"foo": {"1": [1, 2]}},
            Dict[str, Dict[int, List[int]]],
        )

        assert not Item.validate_against(
            {"foo": {1: "foobar"}},
            Dict[str, Dict[int, List[int]]],
        )

    def test_any(self):
        assert Item.validate_against(True, Any)
        assert Item.validate_against(None, Any)
        assert Item.validate_against(1, Any)
        assert Item.validate_against("1", Any)
        assert Item.validate_against([1], Any)
        assert Item.validate_against(["1"], Any)
        assert Item.validate_against({1: 1}, Any)
        assert Item.validate_against({1: "1"}, Any)
        assert Item.validate_against({"1": 1}, Any)
        assert Item.validate_against({"1": "1"}, Any)


class TestItemValidate(TestCase):
    """
    Test <item>.validate
    """

    def test_int(self):
        pig: Item = Item(None, False, int)

        assert pig.validate(1)
        assert not pig.validate("1")

    def test_list_int(self):
        pig: Item = Item(None, False, List[int])

        assert pig.validate([1, 2, 3])
        assert not pig.validate([1, "2", 3])
        assert not pig.validate({1: 2, 2: 3})

    def test_dict_int_str(self):
        pig: Item = Item(None, False, Dict[int, str])

        assert pig.validate({1: "foo", 2: "foobar"})
        assert not pig.validate({1: 1, 2: "foobar"})
        assert not pig.validate([1, "foo", 2, "foobar"])
        assert not pig.validate({1: "foo", "2": "foobar"})

    def test_any(self):
        pig: Item = Item(None, False, Any)

        assert pig.validate(True)
        assert pig.validate(None)
        assert pig.validate(1)
        assert pig.validate("1")
        assert pig.validate([1])
        assert pig.validate(["1"])
        assert pig.validate({1: 1})
        assert pig.validate({1: "1"})
        assert pig.validate({"1": 1})
        assert pig.validate({"1": "1"})
