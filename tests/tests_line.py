from unittest import TestCase

from line import Line


class TestLine(TestCase):

    def test_is_multiple_of_5(self) -> None:
        line = Line(content="")
        self.assertTrue(line.is_multiple_of_5)

    def test_has_dollar_sign(self) -> None:
        line = Line(content="Match 95687 has fin$shed")
        self.assertTrue(line.has_dollar_sign)
