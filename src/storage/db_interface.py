from abc import ABC, abstractmethod
from typing import NamedTuple
from dataclasses import dataclass


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


class UserDBInterface(ABC):

    @abstractmethod
    def select_all(self):
        pass

    @abstractmethod
    def select_user(self, user_id: int):
        pass

    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def add_letter(self):
        pass

    @abstractmethod
    def exists(self) -> bool:
        pass

    @abstractmethod
    def set_level(self, level: str):
        pass


@dataclass
class User:
    user_id: int
    username: str = ''
    first_name: str = ''
    last_name: str = ''
    letter: str = ''
    level: str = ''
