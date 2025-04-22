from pyrogram import Client, filters
from pyrogram.types import Message
from utils import create_welcome_image
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client("welcome-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(filters.new_chat_members)
async def welcome_new_member(_, message: Message):
    for user in message.new_chat_members:
        photo = await bot.download_media(user.photo.big_file_id) if user.photo else "default.jpg"
        image = create_welcome_image(photo, user.first_name, user.username, user.id)
        await message.reply_photo(image, caption=f"Welcome {user.mention}!")

bot.run()