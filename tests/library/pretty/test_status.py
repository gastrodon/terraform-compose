from typing import List
from unittest import TestCase

from library.pretty.status import Animation


class TestStatusAnimation(TestCase):
    """
    Test pretty status animations
    """

    def test_render_incrementing(self):
        pig: Animation = Animation("name")

        plan_order: List[str] = [
            "planning name  . ",
            "planning name   .",
            "planning name  . ",
            "planning name .  ",
            "planning name  . ",
            "planning name   .",
        ]

        for frame in plan_order:
            assert pig.dot_next.render(0) == frame

        apply_order: List[str] = [
            "applying name  . ",
            "applying name .  ",
            "applying name  . ",
            "applying name   .",
            "applying name  . ",
            "applying name .  ",
        ]

        pig.phase_next
        for frame in apply_order:
            assert pig.dot_next.render(0) == frame

        assert pig.finished.render(0) == "applying name ..."
