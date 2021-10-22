import enum
from enum import Enum
from typing import Dict

from library.config.defaults import APPLY, DESTROY, INIT, PLAN
from library.types.item import Item


class Kind(Enum):
    apply = enum.auto()
    destroy = enum.auto()
    plan = enum.auto()
    init = enum.auto()

    @property
    def schema(self) -> Dict[str, Item]:
        return {
            Kind.apply: APPLY,
            Kind.destroy: DESTROY,
            Kind.plan: PLAN,
            Kind.init: INIT,
        }[self]
