import os
import threading

from flask import Flask
from openai import AsyncOpenAI
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters


TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

client = AsyncOpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)


@app.route("/")
def home():
    return "UNKNOWN WORLD AI BOT is running!"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌎 Welcome to UNKNOWN WORLD AI\n\n"
        "Ask me anything!"
    )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = await client.responses.create(
            model="gpt-5.6-luna",
            input=update.message.text
        )

        await update.message.reply_text(response.output_text)

    except Exception as e:
        print("ERROR:", e)
        await update.message.reply_text(
            "Sorry, something went wrong. Please try again."
        )


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


async def run_bot():
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )

    await application.initialize()
    await application.start()
    await application.updater.start_polling()

    while True:
        await __import__("asyncio").sleep(3600)


def main():
    web_thread = threading.Thread(target=run_web, daemon=True)
    web_thread.start()

    import asyncio
    asyncio.run(run_bot())


if __name__ == "__main__":
    main()
