from unittest import TestCase

from line import Line


class TestLine(TestCase):

    def test_is_multiple_of_5(self) -> None:
        line = Line(content="")
        self.assertTrue(line.is_multiple_of_5)

    def test_has_dollar_sign(self) -> None:
        line = Line(content="Match 95687 has fin$shed")
        self.assertTrue(line.has_dollar_sign)

    def test_has_ending_point(self) -> None:
        line = Line(
            content='{"player": {"first_name": "Luis", "last_name": "Suárez", "Age": 34}, "team": "Atlético Madrid"}.',
        )
        self.assertTrue(line.has_ending_point)

        line = Line(
            content='{"player": {"first_name": "Luis", "last_name": "Suárez", "Age": 34}, "team": "Atlético '
                    'Madrid"}.\n\r',
        )
        self.assertTrue(line.has_ending_point)

    def test_has_curly_bracket_at_start(self):
        line = Line(
            content='{"player": {"first_name": "Kylian", "last_name": "Mbappé", "Age": 22}, "team": "PSG"}',
        )
        self.assertTrue(line.has_curly_bracket_at_start)
