from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🤖 AI Assistant", callback_data="ai"),
            InlineKeyboardButton("🎓 Learn Languages", callback_data="languages"),
        ],
        [
            InlineKeyboardButton("💰 Learn & Earn", callback_data="earn"),
            InlineKeyboardButton("📚 Education", callback_data="education"),
        ],
        [
            InlineKeyboardButton("📷 Images", callback_data="images"),
            InlineKeyboardButton("📄 Files & PDF", callback_data="files"),
        ],
        [
            InlineKeyboardButton("🎙️ Voice", callback_data="voice"),
            InlineKeyboardButton("🌐 Web Search", callback_data="search"),
        ],
        [
            InlineKeyboardButton("🖼️ Create Image", callback_data="create_image"),
            InlineKeyboardButton("🎬 Content Tools", callback_data="content"),
        ],
        [
            InlineKeyboardButton("👤 My Account", callback_data="account"),
            InlineKeyboardButton("⭐ Premium", callback_data="premium"),
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
            InlineKeyboardButton("❓ Help", callback_data="help"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def back_button():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🔙 Back to Main Menu", callback_data="main_menu")]]
    )
