from telegram import Update
from telegram.ext import ContextTypes

from services.ai import ask_ai


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    user_text = update.message.text.strip()

    if not user_text:
        return

    try:
        answer = await ask_ai(user_text)

        if not answer:
            answer = "⚠️ Sorry, I couldn't generate an answer."

        await update.message.reply_text(answer)

    except Exception:
        await update.message.reply_text(
            "⚠️ Sorry, something went wrong.\n"
            "Please try again in a moment."
        )
