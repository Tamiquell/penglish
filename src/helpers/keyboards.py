from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


start_keyboard = [
    ['/nouns', '/adverbs'],
    ['/verbs', '/adjectives']
]
start_markup = ReplyKeyboardMarkup(
    start_keyboard,
    one_time_keyboard=False,
    resize_keyboard=True)


verbs_keyboard = [['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                  ['h', 'i', 'j', 'k', 'l', 'm', 'n'],
                  ['o', 'p', 'q', 'r', 's', 't', 'u'],
                  ['v', 'w', 'x', 'y', 'z', 'back']]  # ← ⮌ 🡐
verb_markup = ReplyKeyboardMarkup(
    verbs_keyboard,
    one_time_keyboard=False,
    resize_keyboard=True)


verbs_letter_keyboard = [['Test\U0001F1F7\U0001F1FA\U0001F1EC\U0001F1E7', '/words'],
                         ['Test\U0001F1EC\U0001F1E7\U0001F1F7\U0001F1FA', '/back']]


verb_letter_markup = ReplyKeyboardMarkup(
    verbs_letter_keyboard,
    one_time_keyboard=False,
    resize_keyboard=True)


verbs_test_by_letter_keyboard = [
    ['/reroll', '/words'],
    ['/answer', '/back']
]


verbs_test_by_letter_markup = ReplyKeyboardMarkup(
    verbs_test_by_letter_keyboard,
    one_time_keyboard=False,
    resize_keyboard=True)
