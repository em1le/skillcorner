from __future__ import annotations

from typing import Generator

from line import Line


class Log:
    def __init__(self, data: Generator[str, None, None]) -> None:
        """ Initialize the log with generator data """
        self.lines: list["Line"] = [Line(content=line, position=index) for index, line in enumerate(data)]
