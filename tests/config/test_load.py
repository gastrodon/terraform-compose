from unittest import TestCase

from pydantic import ValidationError

from library import config
from library.types.config import Config


class TestLoad(TestCase):
    """
    Test config loading functions
    """

    def test_raw_loads(self):
        source = """
        services:
            foobar:
                no-destroy: yes
        """

        target = {"foobar": Config(no_destroy=True)}

        assert config.from_raw([], source)["foobar"].no_destroy

    def test_raw_fails_on_type(self):
        source = """
        services:
            foobar:
                no-destroy: oops
        """

        try:
            config.from_raw([], source)

            raise AssertionError("Parser.raw didn't raise")
        except ValidationError:
            return
