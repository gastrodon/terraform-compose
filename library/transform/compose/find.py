import re
from typing import Dict, List

from library.transform.compose.flatten import flatten

never = re.compile("(?!x)x")
noop = lambda it: it


def matches(key, value, key_re, value_re, separator):
    return key_re.match(separator.join(key)) or value_re.match(value)


def find(source: Dict, key=None, value=None, separator=".") -> List[str]:
    """
    Given a source dict and regex key / value matchers,
    return paths that match our criteria

    For path matching, paths are joined with separator before checking
    """
    if key is None and value is None:
        return []

    key_re = re.compile(key) if key else never
    value_re = re.compile(value) if value else never

    return [
        path
        for path, value in flatten(source)
        if matches(path, value, key_re, value_re, separator)
    ]
