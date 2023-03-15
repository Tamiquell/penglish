from telegram import Update
from telegram.ext import ContextTypes

from src.models.verbs import verbsBlock
from src.helpers import keyboards


async def verbs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = 'This is a verbs block'
    await update.message.reply_text(txt,
                                    reply_markup=keyboards.verb_markup)
