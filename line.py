from dataclasses import dataclass


@dataclass
class Line:
    content: str
    position: int = 0
