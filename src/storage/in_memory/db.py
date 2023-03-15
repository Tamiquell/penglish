import random

from src.storage.db_interface import InterfaceDB, Words
import os


class VerbsDB(InterfaceDB):
    def __init__(self) -> None:

        self.english_words, self.rus_words = [], []
        with open('src/storage/in_memory/verbs.txt', 'r', encoding='utf8') as file:
            data = file.read().split('\n')
            for pair in data:
                e, r = pair.split(' - ')
                self.english_words.append(e)
                self.rus_words.append(r)
        assert len(self.english_words) == len(
            self.rus_words), "lists don't match"

    def get_all_data(self) -> Words:
        return Words(self.english_words, self.rus_words)

    def generate_big_test(self):
        indices = list(range(len(self.english_words)))
        random.shuffle(indices)
        return [self.english_words[i] for i in indices], [self.rus_words[i] for i in indices]

    def generate_letter_test(self, letter: str):
        pass


verbsDB = VerbsDB()
