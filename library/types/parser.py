import enum
from dataclasses import dataclass
from enum import IntEnum
from typing import Callable, Dict, List

import yaml

from library.types.config import Config
from library.types.error import ValidationError


def with_middleware(args: List, config: str, middleware: List) -> Dict:
    """
    Given some raw config string, a list of arguments, and middleware;
    pass the config and args through every middleware in order.

    Any raised exceptions stop middleware propagation!
    """

    index = 0
    config_writable = f"{config}"

    for it in (it.callable for it in middleware):
        try:
            config_writable = it(args, config_writable)
        except ValidationError as err:
            print("{middleware[index].__name__} ( #{index} ) failed!")
            print(err.message)

            sys.exit(1)

    return yaml.safe_load(config_writable) or {}


class Order(IntEnum):
    PRE_LOAD = enum.auto()
    LOAD = enum.auto()
    POST_LOAD = enum.auto()
    FINAL = enum.auto()


@dataclass
class Middleware:
    callable: Callable[[str], str]
    order: Order


class Parser:
    def __init__(self):
        self._middleware = []
        self._load = None
        self._final = None

    def middleware(self, order: Order):
        def inner(callable):
            self._middleware += [Middleware(callable=callable, order=order)]

        if order >= Order.POST_LOAD:
            return lambda it: yaml.dump(callable(yaml.safe_load(it)))

        return inner

    def raw(self, args: List, config: str):
        config = with_middleware(args, config, self._middleware)

        return {
            key: Config.parse_obj(value)
            for key, value in config.get("services", {}).items()
        }
