from unittest import TestCase

from line import Line


class TestLine(TestCase):

    def test_is_multiple_of_5(self) -> None:
        line = Line(content="")
        self.assertTrue(line.is_multiple_of_5)


