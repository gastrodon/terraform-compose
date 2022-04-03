from library.transform import compose

cases = [
    {
        "source": {"hello": "world"},
        "include": {"world": "hello"},
        "want": {"hello": "world", "world": "hello"},
    },
    {
        "source": {"hello"},
        "include": {"world"},
        "want": {"hello", "world"},
    },
    {
        "source": {"hello"},
        "include": {"world", "hello"},
        "want": {"hello", "world"},
    },
    {
        "source": {"hello": "there"},
        "include": {"hello": "world"},
        "want": {"hello": "world"},
    },
    {
        "source": {"hello": ["there"]},
        "include": {"hello": ["world"]},
        "want": {"hello": ["there", "world"]},
    },
    {
        "source": {"hello": {"there"}},
        "include": {"hello": {"world"}},
        "want": {"hello": {"there", "world"}},
    },
    {
        "source": {"head": {"child": {"another"}}},
        "include": {"head": {"parent": {"yet some other"}}},
        "want": {"head": {"child": {"another"}, "parent": {"yet some other"}}},
    },
    {
        "source": {"very": {"very": {"very": "nested"}}},
        "include": {"very": {"very": {"also": "important"}}},
        "want": {"very": {"very": {"very": "nested", "also": "important"}}},
    },
]


def test_merge():
    for case in cases:
        assert compose.merge(case["source"], case["include"]) == case["want"]
