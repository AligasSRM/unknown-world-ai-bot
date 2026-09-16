from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


LANGUAGES = {
    "english": ("🇬🇧 English", "Hello", "Hello! How are you?"),
    "german": ("🇩🇪 German", "Hallo", "Hallo! Wie geht es dir?"),
    "swedish": ("🇸🇪 Swedish", "Hej", "Hej! Hur mår du?"),
    "thai": ("🇹🇭 Thai", "สวัสดี", "สวัสดี! สบายดีไหม?"),
    "chinese": ("🇨🇳 Chinese", "你好", "你好！你好吗？"),
    "spanish": ("🇪🇸 Spanish", "Hola", "¡Hola! ¿Cómo estás?"),
}


def language_menu():
    keyboard = [
        [
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_english"),
            InlineKeyboardButton("🇩🇪 German", callback_data="lang_german"),
        ],
        [
            InlineKeyboardButton("🇸🇪 Swedish", callback_data="lang_swedish"),
            InlineKeyboardButton("🇹🇭 Thai", callback_data="lang_thai"),
        ],
        [
            InlineKeyboardButton("🇨🇳 Chinese", callback_data="lang_chinese"),
            InlineKeyboardButton("🇪🇸 Spanish", callback_data="lang_spanish"),
        ],
        [
            InlineKeyboardButton(
                "🔙 Back",
                callback_data="main_menu"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def languages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    if query:
        await query.answer()

        await query.edit_message_text(
            "🎓 Learn Languages\n\n"
            "اختر اللغة التي تريد تعلمها:",
            reply_markup=language_menu(),
        )


async def language_lesson(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.callback_query

    if not query:
        return

    await query.answer()

    language = query.data.replace("lang_", "")

    if language not in LANGUAGES:
        return

    name, word, sentence = LANGUAGES[language]

    await query.edit_message_text(
        f"{name}\n\n"
        f"📚 Lesson 1\n\n"
        f"🔤 Word:\n{word}\n\n"
        f"🗣️ Example:\n{sentence}\n\n"
        "💡 كرر الكلمة والجملة بصوت عالٍ.\n\n"
        "🚧 المزيد من الدروس قيد التطوير.",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🔙 Languages",
                    callback_data="languages"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 Main Menu",
                    callback_data="main_menu"
                )
            ],
        ]),
    )
