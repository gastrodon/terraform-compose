import re
from typing import Dict

from library.transform.compose.flatten import flatten

never = re.compile("(?!x)x")
noop = lambda it: it


def matches(key, value, key_re, value_re, seperator):
    return key_re.match(seperator.join(key)) or value_re.match(value)


def find(source: Dict, key=None, value=None, transformer=noop, seperator=".") -> Dict:
    if key is None and value is None and transformer is noop:
        return source

    key_re = re.compile(key) if key else never
    value_re = re.compile(value) if value else never

    return [
        [path, transformer(value)]
        for path, value in flatten(source)
        if matches(path, value, key_re, value_re, seperator)
    ]

    # return widen.widen(
    #     [
    #         [path, transformer(value)]
    #         for path, value in flatten.flatten(source)
    #         if matches(path, value, key_re, value_re, seperator)
    #     ]
    # )
