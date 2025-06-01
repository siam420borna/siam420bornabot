import asyncio
from pyrogram import Client, filters
from config import Config
from plugins import start, settings

app = Client(
    "video_downloader_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

app.add_handler(start.start_handler)
app.add_handler(settings.settings_handler)

if __name__ == "__main__":
    print("Bot started...")
    app.run()