import os
import random
import re
import string
from dotenv import load_dotenv
import logging
from telegram.constants import ParseMode
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from src.handlers import verbs, common
from src.helpers.keyboards import start_markup
from src.storage.in_memory.db import usersDB
from src.storage.db_interface import User


load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = User(user_id=update.effective_chat.id,
                level='start',
                username=update.effective_chat.username,
                first_name=update.effective_chat.first_name,
                last_name=update.effective_chat.last_name)
    usersDB.add_user(user)
    txt = 'English tg-bot.\nPress /help to get more info'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt, reply_markup=start_markup)


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = User(user_id=update.effective_chat.id,
                level='start',
                username=update.effective_chat.username,
                first_name=update.effective_chat.first_name,
                last_name=update.effective_chat.last_name)
    usersDB.add_user(user)
    txt = "Here are some commands:\n" + \
        "/verbs - ...\n" + \
        "/nouns - ...\n" + \
        "/adverbs - ...\n" + \
        "/adjectives - ...\n"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt, reply_markup=start_markup)


async def nouns(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = 'Nouns block.\nNot implemented yet.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt, reply_markup=start_markup)


async def adverbs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = 'Adverbs block.\nNot implemented yet.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt, reply_markup=start_markup)


async def adjectives(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = 'Adjectives block.\nNot implemented yet.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt, reply_markup=start_markup)


async def checker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    txt = 'You have to generate test first👉👈'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=txt, reply_markup=start_markup)


COMMAND_HANDLERS = {
    "start": start,
    "help": help,
    "verbs": verbs.verbs,
    "nouns": nouns,
    "adverbs": adverbs,
    "adjectives": adjectives,
    "answer": common.answer
}

if __name__ == '__main__':

    application = ApplicationBuilder().token(TOKEN).build()

    for command_name, command_handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(command_name, command_handler))

    application.add_handler(MessageHandler(
        filters.Regex(r'Test'), verbs.test_verbs_by_letter)
    )

    application.add_handler(MessageHandler(
        filters.Regex(r'check'), checker)
    )

    application.add_handler(MessageHandler(
        filters.Regex(r'[abcdefghijklmnopqrstuvwxyz]'), verbs.verbs_by_letter)
    )

    application.run_polling()
