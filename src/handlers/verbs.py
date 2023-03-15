from telegram import Update
from telegram.ext import ContextTypes

from src.helpers import keyboards
from src.helpers.utils import parse_before_print, parse_test_handler, parse_single_array
from src.models.verbs import verbsBlock
from src.storage.in_memory.db import usersDB, answers
from src.storage.db_interface import User
from src.models.levels import Level


async def verbs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = 'This is a verbs block'
    await update.message.reply_text(text,
                                    reply_markup=keyboards.verb_markup)


# TODO add level to usersDB.add_letter
async def verbs_by_letter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    letter = update.message.text
    usersDB.add_letter(update.effective_chat.id, letter=letter)
    usersDB.set_level(update.effective_chat.id,
                      level=Level.test_verbs_by_letter.value)

    eng_words, rus_words = verbsBlock.get_data_on_letter(letter=letter)
    if len(eng_words) > 0:
        text = parse_before_print(eng_words, rus_words)
        await update.message.reply_text(text,
                                        reply_markup=keyboards.verb_letter_markup)
    else:
        if len(letter) == 1:
            await update.message.reply_text("No words on this letter yet🙃. Stay tuned for further updates",
                                            reply_markup=keyboards.verb_markup)
        else:
            await update.message.reply_text("Invalid input. Use interface properly",
                                            reply_markup=keyboards.verb_markup)


async def test_verbs_by_letter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    language = parse_test_handler(update.message.text)
    user = usersDB.select_user(user_id)
    eng, rus = verbsBlock.test_letter(user.letter)
    if language == 'ru':
        questions = parse_single_array(rus)
        answers.verbs_by_letter[user_id] = parse_single_array(eng)
        await update.message.reply_text(questions,
                                        reply_markup=keyboards.verbs_test_by_letter_markup)
    if language == 'en':
        questions = parse_single_array(eng)
        answers.verbs_by_letter[user_id] = parse_single_array(rus)
        await update.message.reply_text(questions,
                                        reply_markup=keyboards.verbs_test_by_letter_markup)
