import enum
from enum import Enum
from typing import Dict

from library.config.defaults import APPLY, DESTROY, PLAN
from library.types.item import Item


class Kind(Enum):
    apply = enum.auto()
    destroy = enum.auto()
    plan = enum.auto()

    @property
    def schema(self) -> Dict[str, Item]:
        return {
            Kind.apply: APPLY,
            Kind.destroy: DESTROY,
            Kind.plan: PLAN,
        }[self]
