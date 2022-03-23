from enum import Enum, auto


class _ParserState(Enum):
    """"""

    ENCODING = auto()
    WORD = auto()
    MEANING_GROUP = auto()


class ThesaurusParser:
    """"""

    def __init__(self, filepath: str) -> None:
        """"""

        self._state = _ParserState.ENCODING
        self.filepath = filepath
        self.encoding = None

        # Read encoding from first line of file
        with open(self.filepath, "r") as f:
            self.encoding = f.readline().strip()
            print(f"{self.encoding=}")

        # Update state (encoding done)
        self._state = _ParserState.WORD

    def parse(self) -> None:
        """"""

        with open(self.filepath, "r", encoding=self.encoding) as f:
            f.readline()  # Discard first line
            print(f.read(255))
