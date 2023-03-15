from telegram import Update
from telegram.ext import ContextTypes

from src.helpers import keyboards
from src.helpers.utils import parse_before_print, parse_test_handler, parse_single_array
from src.models.verbs import verbsBlock
from src.storage.in_memory.db import usersDB, answers
from src.storage.db_interface import User
from src.models.levels import Level


# TODO add logs
async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = usersDB.select_user(update.effective_chat.id)
    match user.level:
        case Level.start.value:
            pass

        case Level.nouns.value:
            pass

        case Level.verbs.value:
            pass

        case Level.adverbs.value:
            pass

        case Level.adjectives.value:
            pass

        case Level.test_all_nouns.value:
            pass

        case Level.test_nouns_by_letter.value:
            pass

        case Level.test_all_verbs.value:
            pass

        case Level.test_verbs_by_letter.value:
            text = answers.verbs_by_letter[user.user_id]
            await update.message.reply_text(text,
                                            reply_markup=keyboards.verb_markup)

        case Level.test_all_adverbs.value:
            pass

        case Level.test_adverbs_by_letter.value:
            pass

        case Level.test_all_adjectives.value:
            pass

        case Level.test_adjectives_by_letter.value:
            pass

        case _:
            text = 'You have to generate test first👉👈'
            await update.message.reply_text(text,
                                            reply_markup=keyboards.verb_markup)
