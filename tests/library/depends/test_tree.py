from typing import Any, Dict, List
from unittest import TestCase

import yaml

from library import depends
from library.types.exceptions import CircularDependsOn

SERVICES_YAML: str = """
services:
    network:
        path: .

    security:
        path: .
        depends-on:
            - network

    cluster:
        path: .
        depends-on:
            - security
            - network

    role:
        path: .

    handler:
        path: .
        depends-on:
            - cluster
            - role
"""

SERVICES_CIRCULAR_YAML: str = """
services:
    network:
        path: .

        depends-on:
            - cluster

    security:
        path: .
        depends-on:
            - network

    cluster:
        path: .
        depends-on:
            - security
"""


class TestDependencyTree(TestCase):
    """
    Test depends.dependency_tree
    """

    def setUp(self):
        self.services: Dict[str, Any] = yaml.safe_load(SERVICES_YAML)["services"]
        self.tree: Dict[str, Any] = depends.dependency_tree("handler", self.services)

    def test_depth(self):
        depth: int = depends.tree_depth(self.tree)

        for service in depends.flat_tree(self.tree):
            assert service["level"] <= depth

    def test_tree_dependencies(self):
        service: str = "cluster"
        targets: List[str] = ["network", "security"]

        tree = depends.dependency_tree(service, self.services)
        dependencies = [*map(lambda it: it["name"], tree["depends-on"])]

        for it in targets:
            assert it in dependencies

    def test_tree_no_circular(self):
        service: str = "cluster"
        services: Dict[str, Any] = yaml.safe_load(SERVICES_CIRCULAR_YAML)["services"]

        try:
            depends.dependency_tree(service, services)
            raise AssertionError

        except CircularDependsOn as err:
            assert err.service == service
            assert service in err.parents


class TestOrderLevels(TestCase):
    """
    Test depends.order_levels
    """

    def setUp(self):
        self.services: Dict[str, Any] = yaml.safe_load(SERVICES_YAML)["services"]
        self.tree: Dict[str, Any] = depends.dependency_tree("handler", self.services)
        self.ordered: List[List[str]] = depends.order_levels([self.tree])

    def test_root_ordered_last(self):
        assert [self.tree["name"]] == self.ordered[-1]

    def test_no_dependencies_first(self):
        no_dependencies = sorted(["role", "network"])

        assert no_dependencies == sorted(self.ordered[0])


class TestOrderFlat(TestCase):
    """
    Test depends.order_flat
    """

    def setUp(self):
        self.services: Dict[str, Any] = yaml.safe_load(SERVICES_YAML)["services"]
        self.tree: Dict[str, Any] = depends.dependency_tree("handler", self.services)
        self.ordered: List[List[str]] = depends.order_flat([self.tree])

    def test_root_ordered_first(self):
        assert self.tree["name"] == self.ordered[-1]

    def test_no_dependencies_first(self):
        no_dependencies = sorted(["role", "network"])

        assert no_dependencies == sorted(self.ordered[0:2])
