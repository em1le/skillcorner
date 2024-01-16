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
