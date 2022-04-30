import re
from typing import Dict, List

from library.transform.compose.flatten import flatten

never = re.compile("(?!x)x")
noop = lambda it: it


def matches(key, value, key_re, value_re, separator):
    key_string = separator.join(map(str, key))

    if isinstance(value, (list, tuple, set)):
        return any(matches(key, it, key_re, value_re, separator) for it in value)

    if not isinstance(value, str) and value_re is never:
        return key_re.match(key_string)

    return key_re.match(key_string) or value_re.match(value)


def find(source: Dict, key=None, value=None, separator=".", lists=True) -> List[str]:
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
        for path, value in flatten(source, lists=lists)
        if matches(path, value, key_re, value_re, separator)
    ]
