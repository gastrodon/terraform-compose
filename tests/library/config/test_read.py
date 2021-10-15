from unittest import TestCase

from library import config
from library.config.kind import Kind
from library.types.exceptions import ValidateFailed


class TestRead(TestCase):
    """
    Test read
    """

    def test_read_plan(self):
        part = {
            "refresh-only": True,
            "target": "service-name",
            "var-files": ["./foo/bar.tfvar"],
            "vars": {
                "var": "foobar",
                "bengis": "hello",
            },
        }

        service_config = {
            **part,
            "refresh": False,
            "replace": None,
        }

        assert config.read(Kind.plan, "name", part) == service_config

    def test_read_plan_fail(self):
        service = "name"
        part = {"var-files": "foobar"}

        try:
            config.read(Kind.plan, service, part)
            raise AssertionError

        except ValidateFailed as err:
            assert err.service == "name"
            assert err.key == "var-files"
            assert err.value == part["var-files"]
