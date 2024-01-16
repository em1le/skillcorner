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

    def test_has_curly_bracket_at_start(self) -> None:
        line = Line(
            content='{"player": {"first_name": "Kylian", "last_name": "Mbappé", "Age": 22}, "team": "PSG"}',
        )
        self.assertTrue(line.has_curly_bracket_at_start)

    def test_process_line_with_multiple_of_5(self) -> None:
        expected_data = "Multiple de 5"
        line = Line(content="")
        self.assertEqual(expected_data, line.process_line())

    def test_process_line_with_dollar_sign(self) -> None:
        expected_data = "Match_95687_has_fin$shed"
        line = Line(content="Match 95687 has fin$shed", position=1)
        self.assertEqual(expected_data, line.process_line())
