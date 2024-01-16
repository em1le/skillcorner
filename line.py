from dataclasses import dataclass


@dataclass
class Line:
    content: str
    position: int = 0

    @property
    def is_multiple_of_5(self) -> bool:
        """Check if number position is a multiple of 5."""
        return self.position % 5 == 0

    @property
    def has_dollar_sign(self) -> bool:
        """Check if line content contains dollar sign."""
        return "$" in self.content

    @property
    def has_ending_point(self) -> bool:
        """Check if line content ends with a period."""
        return self.content.rstrip("\r\n").endswith(".")

    @property
    def has_curly_bracket_at_start(self) -> bool:
        """Check if line content starts with a curly bracket."""
        return self.content.startswith("{")

    def process_line(self) -> str:
        """Process line according to specific condition and return value accordingly."""
        if self.is_multiple_of_5:
            return "Multiple de 5"
        elif self.has_dollar_sign:
            return self.content.strip().replace(" ", "_")
