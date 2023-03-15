from src.models.interface import Branch
from src.storage.in_memory.db import verbsDB


class Verbs(Branch):
    def __init__(self):
        self.data = []
        res = verbsDB.get_all_data()
        self.eng_words, self.rus_words = res.english, res.russian

    def get_all_data(self) -> tuple[list[str], list[str]]:
        return self.eng_words, self.rus_words

    def get_data_on_letter(self, letter: str) -> tuple[list[str], list[str]]:
        indices = [i for i in range(len(self.eng_words))
                   if self.eng_words[i][3] == letter]
        return ([self.eng_words[i] for i in indices],
                [self.rus_words[i] for i in indices])

    def test_all(self):
        pass

    def test_letter(self):
        pass

    def reroll(self):
        pass

    def answer(self):
        pass

    def next(self):
        pass

    def print_all(self):
        pass


verbsBlock = Verbs()
