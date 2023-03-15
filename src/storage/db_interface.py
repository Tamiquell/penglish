from abc import ABC, abstractmethod
from typing import NamedTuple


class InterfaceDB(ABC):

    @abstractmethod
    def get_all_data(self):
        pass

    @abstractmethod
    def generate_big_test(self):
        pass

    @abstractmethod
    def generate_letter_test(self, letter: str):
        pass


class Words(NamedTuple):
    english: list[str]
    russian: list[str]
