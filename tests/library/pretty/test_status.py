from unittest import TestCase

from library.pretty import Status


class TestStatusStatus(TestCase):
    """
    Test pretty status animations
    """

    def test_render_incrementing(self):
        name: str = "service"
        pig: Status = Status(name)

        assert pig.render(0) == f"planning {name} ..."
        assert pig.phase_next().render(0) == f"applying {name} ..."
        assert pig.finish().render(0) == f"applying {name}   ✓"
