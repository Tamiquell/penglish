from src.helpers.exceptions import WrongTestHandler


def parse_test_handler(text: str) -> str:
    """returns language mode for test generation"""
    if len(text) > 4:
        if text[-2:] == '🇬🇧':
            return 'ru'
        elif text[-2:] == '🇷🇺':
            return 'en'
        else:
            raise WrongTestHandler("Wrong test handler")
    else:
        raise WrongTestHandler("Wrong test handler")


def parse_before_print(arr1, arr2):
    return '\n'.join(
        [' - '.join(i) for i in zip(arr1, arr2)])


def parse_single_array(arr):
    return '\n'.join(arr)
