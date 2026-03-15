from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = "8753224445:AAGQ-Ww00JadUJSpiev1o0mQYRK9KdcOHIM"
GROUP_ID = -1003632901634

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Игнорируем сообщения из группы
    if update.effective_chat.id == GROUP_ID:
        return

    user = update.message.from_user

    header = f"""
Новое сообщение

Имя: {user.first_name}
Username: @{user.username if user.username else 'нет'}
"""

    # Текст
    if update.message.text:
        text = f"{header}\nСообщение:\n{update.message.text}"
        await context.bot.send_message(chat_id=GROUP_ID, text=text)

    # Фото
    elif update.message.photo:
        photo = update.message.photo[-1].file_id
        await context.bot.send_photo(chat_id=GROUP_ID, photo=photo, caption=header)

    # Документы
    elif update.message.document:
        file_id = update.message.document.file_id
        await context.bot.send_document(chat_id=GROUP_ID, document=file_id, caption=header)

    # Видео
    elif update.message.video:
        file_id = update.message.video.file_id
        await context.bot.send_video(chat_id=GROUP_ID, video=file_id, caption=header)

    # Аудио
    elif update.message.audio:
        file_id = update.message.audio.file_id
        await context.bot.send_audio(chat_id=GROUP_ID, audio=file_id, caption=header)


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, forward))

app.run_polling()
