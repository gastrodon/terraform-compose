from abc import ABC
from typing import List

from library.model import Compose


class Command(ABC):
    @staticmethod
    def arguments() -> List[str]:
        """
        A collection of arguments that are relevent to this particular command
        """
        raise NotImplementedError()

    @staticmethod
    def compile(compose: Compose) -> List[List[str]]:
        """
        Given a Compose document, compile it into a collection of shell commands
        """
        raise NotImplementedError()
