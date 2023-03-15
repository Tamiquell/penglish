from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


verbs_keyboard = [['a', 'b', 'c', 'd', 'e', 'f', 'g'],
                  ['h', 'i', 'j', 'k', 'l', 'm', 'n'],
                  ['o', 'p', 'q', 'r', 's', 't', 'u'],
                  ['v', 'w', 'x', 'y', 'z', '', 'back']]
verb_markup = ReplyKeyboardMarkup(
    verbs_keyboard,
    one_time_keyboard=False,
    resize_keyboard=True)
