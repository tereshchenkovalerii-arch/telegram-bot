from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")
GROUP_ID = int(os.environ.get("GROUP_ID"))

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == GROUP_ID:
        return

    user = update.message.from_user
    header = f"""
Новое сообщение

Имя: {user.first_name}
Username: @{user.username if user.username else 'нет'}
"""
    if update.message.text:
        text = f"{header}\nСообщение:\n{update.message.text}"
        await context.bot.send_message(chat_id=GROUP_ID, text=text)
    elif update.message.photo:
        photo = update.message.photo[-1].file_id
        await context.bot.send_photo(chat_id=GROUP_ID, photo=photo, caption=header)
    elif update.message.document:
        file_id = update.message.document.file_id
        await context.bot.send_document(chat_id=GROUP_ID, document=file_id, caption=header)
    elif update.message.video:
        file_id = update.message.video.file_id
        await context.bot.send_video(chat_id=GROUP_ID, video=file_id, caption=header)
    elif update.message.audio:
        file_id = update.message.audio.file_id
        await context.bot.send_audio(chat_id=GROUP_ID, audio=file_id, caption=header)

app = ApplicationBuilder().token(TOKEN).build()
print("Бот запущен и работает...")
app.add_handler(MessageHandler(filters.ALL, forward))
app.run_polling()
