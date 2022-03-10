from dataclasses import dataclass
from types import Dict, List, Union

from library.config.middleware.parser import parser
from library.types.parser import Order


@dataclass
class AtFile:
    config_path: str
    file_path: str

    def read(self) -> str:
        with open(self.file_path) as stream:
            return stream.read()


def gather_at_files(prefix: str, group: Union[List, Dict]):
    return


@parser.middleware(Order.POST_LOAD)
def at_files(args, config):
    return
