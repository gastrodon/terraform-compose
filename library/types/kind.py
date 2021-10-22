import enum
from enum import Enum
from typing import Dict

from library.config.defaults import APPLY, DESTROY, INIT, OUTPUT, PLAN, REFRESH
from library.types.item import Item


class Kind(Enum):
    apply = enum.auto()
    destroy = enum.auto()
    init = enum.auto()
    output = enum.auto()
    plan = enum.auto()
    refresh = enum.auto()

    @property
    def schema(self) -> Dict[str, Item]:
        return {
            Kind.apply: APPLY,
            Kind.destroy: DESTROY,
            Kind.init: INIT,
            Kind.output: OUTPUT,
            Kind.plan: PLAN,
            Kind.refresh: REFRESH,
        }[self]
