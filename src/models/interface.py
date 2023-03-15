from abc import ABC, abstractmethod


class Branch(ABC):
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def get_all_data(self):
        pass

    @abstractmethod
    def get_data_on_letter(self, letter: str):
        pass

    @abstractmethod
    def test_all(self):
        pass

    @abstractmethod
    def test_letter(self):
        pass
