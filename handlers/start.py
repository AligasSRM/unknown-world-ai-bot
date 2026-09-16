import logging

from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("START RECEIVED")

    message = update.effective_message

    if message is None:
        logger.error("No message found")
        return

    await message.reply_text(
        "🌎 Welcome to UNKNOWN WORLD AI\n\n"
        "🤖 Your AI Super Assistant\n\n"
        "Choose a service from the menu below:",
        reply_markup=main_menu(),
    )
