import json  # noqa

import yaml

from library import depends  # noqa

with open("terraform-compose.yml") as stream:
    config = yaml.safe_load(stream)

trees = [
    depends.tree("cluster", config["services"]),
    depends.tree("services", config["services"]),
]


def flat_tree(_tree):
    return [{"name": _tree["name"], "level": _tree["level"]}] + [
        item
        for flattened in [flat_tree(it) for it in _tree["depends-on"]]
        for item in flattened
    ]


def collect_levels(trees):
    services_flat = [
        service
        for flattened in [flat_tree(it) for it in trees]
        for service in flattened
    ]
    level_max = max(it["level"] for it in services_flat)
    collected = [set() for _ in range(level_max + 1)]

    # TODO use sets
    for service in services_flat:
        collected[service["level"]].add(service["name"])

    return [*map(list, collected)]
