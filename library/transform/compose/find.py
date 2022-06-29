import re
from typing import Dict, List

from library.transform.compose.flatten import flatten

always = re.compile(".*")
noop = lambda it: it


def matches(key, value, key_re, value_re, separator):
    key_string = separator.join(map(str, key))

    if isinstance(value, (list, tuple, set)):
        return any(matches(key, it, key_re, value_re, separator) for it in value)

    if not isinstance(value, str) and value_re is always:
        return key_re.match(key_string)

    if isinstance(value, bool):
        return key_re.match(key_string) and value_re.match(str(value))

    return key_re.match(key_string) and value_re.match(value)


def find(source: Dict, key=None, value=None, separator=".", lists=True) -> List[str]:
    """
    Given a source dict and regex key / value matchers,
    return paths that match our criteria

    For path matching, paths are joined with separator before checking
    """
    if key is None and value is None:
        return []

    key_re = re.compile(key) if key else always
    value_re = re.compile(value) if value else always

    return [
        path
        for path, value in flatten(source, lists=lists)
        if matches(path, value, key_re, value_re, separator)
    ]
