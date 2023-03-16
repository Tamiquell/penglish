from enum import Enum


class Level(Enum):
    start = "start"

    nouns = "nouns"
    verbs = "verbs"
    adverbs = "adverbs"
    adjectives = "adjectives"

    nouns_by_letter = "nouns_by_letter"
    verbs_by_letter = "verbs_by_letter"
    adverbs_by_letter = "adverbs_by_letter"
    adjectives_by_letter = "adjectives_by_letter"

    test_all_nouns = "test_all_nouns"
    test_nouns_by_letter = "test_nouns_by_letter"

    test_all_verbs = "test_all_verbs"
    test_verbs_by_letter = "test_verbs_by_letter"

    test_all_adverbs = "test_all_adverbs"
    test_adverbs_by_letter = "test_adverbs_by_letter"

    test_all_adjectives = "test_all_adjectives"
    test_adjectives_by_letter = "test_adjectives_by_letter"
