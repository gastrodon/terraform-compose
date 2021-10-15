from typing import Any, Dict, List, _GenericAlias


class Item:
    def __init__(self, default: Any, required: bool, type: Any):
        self.default = default
        self.required = required
        self.type = type

    @classmethod
    def validate_against(self, value: Any, type: Any) -> bool:
        if type == Any:
            return True

        if isinstance(type, _GenericAlias):
            if type.__origin__ == list and isinstance(value, list):
                return all(
                    [self.validate_against(it, type.__args__[0]) for it in value]
                )

            if type.__origin__ == dict and isinstance(value, dict):
                return all(
                    [
                        self.validate_against(key, type.__args__[0])
                        and self.validate_against(value, type.__args__[1])
                        for key, value in value.items()
                    ]
                )
        else:
            return isinstance(value, type)

        return False

    def validate(self, value: Any) -> bool:
        return self.validate_against(value, self.type)


APPLY: Dict[str, Item] = {
    "auto-approve": Item(False, False, bool),
    "color": Item(True, False, bool),
    "compact-warnings": Item(False, False, bool),
    "lock": Item(False, False, bool),
    "state-backup": Item(None, False, str),
    "state-out": Item(None, False, str),
    "state-path": Item(None, False, str),
    "parallelism": Item(10, False, int),
}

DESTROY: Dict[str, Item] = {**APPLY}

PLAN: Dict[str, Item] = {
    "refresh-only": Item(False, False, bool),
    "refresh": Item(False, False, bool),
    "replace": Item(None, False, str),
    "target": Item(None, False, str),
    "var-files": Item([], False, List[str]),
    "vars": Item({}, False, [Dict[str, str]]),
}
