import random
import logging

from src.storage.db_interface import InterfaceDB, Words, UserDBInterface, User
import os
from src.storage.db_interface import User


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


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


class UsersDB(UserDBInterface):

    def __init__(self) -> None:
        self.users: dict[int, User] = {}

    def select_all(self):
        return self.users

    def select_user(self, user_id: int):
        return self.users[user_id]

    def add_user(self, user: User):
        if not self.exists(user.user_id):
            self.users[user.user_id] = user
            logging.info(
                f"Added user: {user.user_id}, user_name: {user.username}, name: {user.first_name} {user.last_name}")

    def add_letter(self, user_id: int, letter: str):
        self.users[user_id].letter = letter

    def exists(self, user_id: int) -> bool:
        if user_id in self.users:
            return True
        return False

    def set_level(self,  user_id: int, level: str):
        self.users[user_id].level = level


usersDB = UsersDB()


class Answers:
    def __init__(self) -> None:
        self.nouns: dict[int, str] = {}
        self.verbs: dict[int, str] = {}
        self.adverbs: dict[int, str] = {}
        self.adjectives: dict[int, str] = {}

        self.nouns_by_letter: dict[int, str] = {}
        self.verbs_by_letter: dict[int, str] = {}
        self.adverbs_by_letter: dict[int, str] = {}
        self.adjectives_by_letter: dict[int, str] = {}


answers = Answers()
