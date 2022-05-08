from abc import ABC
from typing import Dict, List

from library.model import Compose
from library.model.cli.argument import Argument


class Command(ABC):
    @staticmethod
    def arguments() -> Dict[str, Argument]:
        """A collection of key: value arguments"""
        return {}

    @staticmethod
    def compile(compose: Compose) -> List[List[str]]:
        """
        Given a Compose document, compile it into a collection of shell commands
        """
        raise NotImplementedError()
