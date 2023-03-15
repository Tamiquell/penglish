from src.models.levels import Level


if __name__ == '__main__':
    s = 'adverbs'

    match s:
        case Level.nouns.name:
            print("noun...")
        case Level.adverbs.name:
            print("adverb...")
