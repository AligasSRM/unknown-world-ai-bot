from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌎 Welcome to UNKNOWN WORLD AI\n\n"
        "🤖 Your AI Super Assistant\n\n"
        "Choose a service from the menu below:",
        reply_markup=main_menu(),
    )
