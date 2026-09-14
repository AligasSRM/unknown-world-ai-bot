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
            "input": (
                "You are UNKNOWN WORLD AI, a smart content assistant. "
                "Help the user create YouTube content, scripts, ideas, "
                "titles, descriptions, hashtags and translations.\n\n"
                f"User: {message}"
            )
        },
        timeout=60
    )

    response.raise_for_status()
    data = response.json()

    return data["output"][0]["content"][0]["text"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في UNKNOWN WORLD AI!\n\n"
        "أنا مساعدك الذكي لصناعة المحتوى والأفكار والسكريبتات والترجمة.\n\n"
        "اكتب لي أي فكرة وسأساعدك."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 UNKNOWN WORLD AI\n\n"
        "/start - بدء البوت\n"
        "/help - المساعدة\n"
        "/content - صناعة محتوى\n"
        "/script - كتابة نص فيديو\n"
        "/translate - ترجمة\n"
        "/ideas - أفكار جديدة\n\n"
        "أو اكتب طلبك مباشرة."
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.chat.send_action("typing")
        answer = ask_ai(update.message.text)
        await update.message.reply_text(answer)
    except Exception:
        await update.message.reply_text(
            "حدث خطأ مؤقتًا. حاول مرة أخرى بعد قليل."
        )


def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("content", message_handler))
    app.add_handler(CommandHandler("script", message_handler))
    app.add_handler(CommandHandler("translate", message_handler))
    app.add_handler(CommandHandler("ideas", message_handler))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
