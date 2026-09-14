import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def ask_ai(message):
    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-5.6-luna",
            "input": f"You are UNKNOWN WORLD AI. Help the user with: {message}"
        },
        timeout=60
    )

    response.raise_for_status()
    data = response.json()

    return data["output"][0]["content"][0]["text"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في UNKNOWN WORLD AI!\n\n"
        "اكتب أي سؤال أو فكرة وسأساعدك."
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        answer = ask_ai(update.message.text)
        await update.message.reply_text(answer)
    except Exception:
        await update.message.reply_text(
            "حدث خطأ مؤقتًا. حاول مرة أخرى."
        )


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    app.run_polling()


if __name__ == "__main__":
    main()
