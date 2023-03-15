import random
from typing import TypeAlias

from src.models.interface import Branch
from src.storage.in_memory.db import verbsDB

English: TypeAlias = list[str]
Russian: TypeAlias = list[str]
TEST_SIZE = 7


class Verbs(Branch):
    def __init__(self):
        self.data = []
        res = verbsDB.get_all_data()
        self.eng_words, self.rus_words = res.english, res.russian

    def get_all_data(self) -> tuple[English, Russian]:
        return self.eng_words, self.rus_words

    def get_data_on_letter(self, letter: str) -> tuple[English, Russian]:
        indices = [i for i in range(len(self.eng_words))
                   if self.eng_words[i][3] == letter]
        return ([self.eng_words[i] for i in indices],
                [self.rus_words[i] for i in indices])

    def test_all(self):
        pass

    def test_letter(self, letter: str) -> tuple[English, Russian]:
        eng_words, rus_words = self.get_data_on_letter(letter)
        indices = random.sample(range(len(eng_words)), TEST_SIZE)
        eng_res: English = [eng_words[i] for i in indices]
        rus_res: Russian = [rus_words[i] for i in indices]
        return eng_res, rus_res

    def reroll(self):
        pass

    def answer(self):
        pass

    def next(self):
        pass

    def print_all(self):
        pass


verbsBlock = Verbs()
