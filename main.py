import os
import random
from dotenv import load_dotenv
import logging
from telegram.constants import ParseMode
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from src.handlers.verbs import verbs

load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CURRENT_LEVEL
    CURRENT_LEVEL = 'Start'
    txt = 'English tg-bot.\nPress /help to get more info'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global CURRENT_LEVEL
    CURRENT_LEVEL = 'Start'
    txt = "Here are some commands:\n" + \
        "/verbs - ...\n" + \
        "/nouns - ...\n" + \
        "/adverbs - ...\n" + \
        "/adjectives - ...\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt)


if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('verbs', verbs))

    # application.add_handler(MessageHandler(
    #     filters.Regex(r'[абгджзимноөстуүхцчшэя]'), letter)
    # )

    application.run_polling()
