from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")
GROUP_ID = int(os.environ.get("GROUP_ID"))

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    text = f"""
Новое сообщение

Имя: {user.first_name}
Username: @{user.username}

Сообщение:
{update.message.text}
"""

    await context.bot.send_message(chat_id=GROUP_ID, text=text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, forward))

app.run_polling()
