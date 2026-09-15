from telegram import Update
from telegram.ext import ContextTypes

from keyboards import back_button


async def earning(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    query = update.callback_query

    if not query:
        return

    await query.edit_message_text(
        "💰 Learn & Earn\n\n"
        "سأساعدك على تعلّم طرق حقيقية وقانونية لتحسين دخلك، مثل:\n\n"
        "💻 العمل عبر الإنترنت\n"
        "🤖 استخدام الذكاء الاصطناعي\n"
        "📱 صناعة المحتوى\n"
        "💼 العمل الحر\n"
        "📚 تطوير المهارات\n"
        "🚀 بناء مشروع رقمي\n\n"
        "اكتب لي ما تريد تعلّمه وسأساعدك خطوة بخطوة.",
        reply_markup=back_button(),
    )
