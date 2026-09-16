import asyncio
import logging
import threading

from flask import Flask
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

from config import TELEGRAM_TOKEN, PORT
from handlers.start import start
from handlers.chat import chat
from handlers.earning import earning
from handlers.languages import languages, language_lesson
from keyboards import main_menu, back_button


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


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


async def button_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query

    if not query:
        return

    await query.answer()

    if query.data == "ai":
        await query.edit_message_text(
            "🤖 AI Assistant\n\n"
            "اكتب سؤالك وسأساعدك.",
            reply_markup=back_button(),
        )

    elif query.data == "languages":
        await languages(update, context)

    elif query.data.startswith("lang_"):
        await language_lesson(update, context)

    elif query.data == "earn":
        await earning(update, context)

    elif query.data == "about":
        await query.edit_message_text(
            "ℹ️ UNKNOWN WORLD AI\n\n"
            "Your AI Super Assistant.\n\n"
            "Powered by artificial intelligence.",
            reply_markup=back_button(),
        )

    elif query.data == "help":
        await query.edit_message_text(
            "❓ Help\n\n"
            "اكتب أي سؤال مباشرة وسأحاول مساعدتك.\n\n"
            "استخدم 🔙 للعودة إلى القائمة الرئيسية.",
            reply_markup=back_button(),
        )

    elif query.data == "main_menu":
        await query.edit_message_text(
            "🌎 UNKNOWN WORLD AI\n\n"
            "Choose a service from the menu below:",
            reply_markup=main_menu(),
        )

    else:
        await query.edit_message_text(
            "🚧 هذه الخدمة قيد التطوير حاليًا.\n\n"
            "سنضيفها قريبًا إلى UNKNOWN WORLD AI.",
            reply_markup=back_button(),
        )


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

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            chat,
        )
    )

    logger.info(
        "Starting UNKNOWN WORLD AI BOT..."
    )

    await application.initialize()
    await application.start()

    await application.updater.start_polling(
        drop_pending_updates=True
    )

    logger.info(
        "Telegram bot is running"
    )

    while True:
        await asyncio.sleep(3600)


def main():

    web_thread = threading.Thread(
        target=run_web,
        daemon=True,
    )

    web_thread.start()

    asyncio.run(run_bot())


if __name__ == "__main__":
    main()
