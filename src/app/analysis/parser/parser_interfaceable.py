
from abc import ABCMeta, abstractmethod


class ParserInterfaceable(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def from_lines_list(cls, lines_list: list[str]) -> "ParserInterfaceable":
        pass
