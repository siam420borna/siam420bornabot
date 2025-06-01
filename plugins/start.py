from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

async def start(_, message: Message):
    await message.reply_text(
        "ðŸ‘‹ Welcome to the Universal Video Downloader Bot!\n\n"
        "Just send me any video or audio link (YouTube, Facebook, Twitter, Mega.nz, etc.)\n"
        "I'll show you all available formats to download.\n\n"
        "Use /settings to customize features like watermark, screenshot, and more."
    )

start_handler = MessageHandler(start, filters.command("start"))
