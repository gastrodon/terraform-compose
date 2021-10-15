from typing import Any, _GenericAlias, _UnionGenericAlias


class Item:
    def __init__(self, default: Any, required: bool, type: Any):
        self.default = default
        self.required = required
        self.type = type

    @classmethod
    def validate_against(self, value: Any, type: Any) -> bool:
        if type == Any:
            return True

        if isinstance(type, _UnionGenericAlias):
            return any(
                [self.validate_against(value, option) for option in type.__args__]
            )

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
