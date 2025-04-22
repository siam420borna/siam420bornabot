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

# Dummy HTTP server to keep Koyeb free instance alive
import threading
import socket

def run_dummy_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8080))
    s.listen(1)
    while True:
        conn, _ = s.accept()
        conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK")
        conn.close()

threading.Thread(target=run_dummy_server, daemon=True).start()

app.run()