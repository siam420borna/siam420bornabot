from pyrogram import Client, filters
from pyrogram.types import Message
from helper.yt_utils import extract_info
from plugins.buttons import generate_buttons

@Client.on_message(filters.text & filters.private)
async def link_handler(client, message: Message):
    url = message.text.strip()
    info = await extract_info(url)
    if not info:
        return await message.reply("❌ Unsupported or broken link.")

    thumb = info.get("thumbnail")
    title = info.get("title")
    buttons = generate_buttons(info)
    caption = f"**{title}**\nDuration: {info.get('duration')} sec"

    await message.reply_photo(photo=thumb, caption=caption, reply_markup=buttons)