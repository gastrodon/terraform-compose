from abc import ABC
from typing import List

from library.model import Compose


class Command(ABC):
    @staticmethod
    def arguments_flag() -> List[str]:
        """A collection of flags"""
        return []

    @staticmethod
    def arguments_kv() -> List[str]:
        """A collection of key: value arguments"""
        return []

    @staticmethod
    def compile(compose: Compose) -> List[List[str]]:
        """
        Given a Compose document, compile it into a collection of shell commands
        """
        raise NotImplementedError()
