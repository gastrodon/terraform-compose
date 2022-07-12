import re
from typing import Dict, List

dicty_split = re.compile(r"(?<!\\)(?:\\\\)*=")


def listy(item: str) -> List[str]:
    return [item]


def dicty(item: str) -> Dict[str, str]:
    key, value = dicty_split.split(item)

    return {key: value}
