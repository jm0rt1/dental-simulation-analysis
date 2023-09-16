
from abc import ABCMeta, abstractmethod
from dataclasses import is_dataclass


class ParserInterfaceable(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def from_lines_list_old(cls, lines_list: list[str]) -> "ParserInterfaceable":
        pass

    @classmethod
    @abstractmethod
    def from_lines_list_new(cls, lines_list: list[str]) -> "ParserInterfaceable":
        pass

    def to_dict(self):
        if is_dataclass(self):
            return {k: self.__to_dict(v) for k, v in self.__dict__.items()}
        else:
            return self

    def __to_dict(self, obj: "ParserInterfaceable"):
        if is_dataclass(obj):
            return obj.to_dict()
        elif isinstance(obj, list):
            return [self.__to_dict(e) for e in obj]
        elif isinstance(obj, dict):
            return {k: self.__to_dict(v) for k, v in obj.items()}
        else:
            return obj
