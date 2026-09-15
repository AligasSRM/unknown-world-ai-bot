import asyncio
import logging
import os
import threading

from flask import Flask
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import TELEGRAM_TOKEN, PORT
from handlers.start import start
from handlers.chat import chat


# =========================
# LOGGING
# =========================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


# =========================
# FLASK WEB SERVER
# =========================

app = Flask(__name__)


@app.route("/")
def home():
    return "UNKNOWN WORLD AI BOT is running!"


@app.route("/health")
def health():
    return "OK"


def run_web():
    app.run(
        host="0.0.0.0",
        port=PORT,
    )


# =========================
# TELEGRAM BOT
# =========================

async def run_bot():
    if not TELEGRAM_TOKEN:
        raise RuntimeError(
            "TELEGRAM_TOKEN is not configured."
        )

    application = (
        Application.builder()
        .token(TELEGRAM_TOKEN)
        .connect_timeout(30)
        .read_timeout(30)
        .write_timeout(30)
        .pool_timeout(30)
        .build()
    )

    # /start
    application.add_handler(
        CommandHandler("start", start)
    )

    # Normal text messages
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            chat,
        )
    )

    logger.info("Starting UNKNOWN WORLD AI BOT...")

    await application.initialize()
    await application.start()
    await application.updater.start_polling(
        drop_pending_updates=True
    )

    logger.info("Telegram bot is running")

    while True:
        await asyncio.sleep(3600)


# =========================
# MAIN
# =========================

def main():
    web_thread = threading.Thread(
        target=run_web,
        daemon=True,
    )

    web_thread.start()

    asyncio.run(run_bot())


if __name__ == "__main__":
    main()
