
from abc import ABCMeta, abstractmethod


class ParserInterfaceable(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def from_lines_list_old(cls, lines_list: list[str]) -> "ParserInterfaceable":
        pass

    @classmethod
    @abstractmethod
    def from_lines_list_new(cls, lines_list: list[str]) -> "ParserInterfaceable":
        pass
