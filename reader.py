from dataclasses import dataclass
from typing import Generator


@dataclass
class Reader:

    @staticmethod
    def extract_data(file_path: str) -> Generator[str, None, None]:
        """ Extract data from file and yield lines """
        with open(file_path, 'r') as f:
            yield from f

