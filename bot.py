import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to TON Meme Trends Promo Bot\n\n"
        "Send your project details in ONE message:\n\n"
        "• Project name\n"
        "• Description\n"
        "• Telegram link\n"
        "• Website (optional)\n"
        "• TX hash\n\n"
        "⚠️ Visibility only. Not financial advice."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    admin_text = (
        "📥 NEW PROMO REQUEST\n\n"
        f"👤 User: @{user.username}\n"
        f"🆔 ID: {user.id}\n\n"
        f"{text}"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=admin_text)
    await update.message.reply_text("✅ Details received. We’ll review it.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
