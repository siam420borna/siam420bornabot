import os
from pyrogram import Client, filters
from pyrogram.types import Message
from utils import create_welcome_image

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("welcome-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.new_chat_members)
async def welcome(_, message: Message):
    for user in message.new_chat_members:
        img = await create_welcome_image(user)
        await message.reply_photo(
            photo=img,
            caption=f"স্বাগতম {user.mention}!\n\nইউজারনেম: @{user.username or 'N/A'}\nইউজার আইডি: `{user.id}`"
        )
        img.close()

app.run()