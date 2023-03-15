from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias

UserId: TypeAlias = int


class Level(Enum):
    start = "start"
    nouns = "nouns"
    verbs = "verbs"
    adjectives = "adjectives"
    adverbs = "adverbs"
    test_all = "test_all"
    test_letter = "test_letter"


@dataclass
class Users:
    users: dict[UserId, Level]
