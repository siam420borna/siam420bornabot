from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import get_user_settings, toggle_user_setting

@Client.on_message(filters.command("settings"))
async def settings_handler(_, message: Message):
    user_id = message.from_user.id
    settings = await get_user_settings(user_id)

    buttons = [
        [InlineKeyboardButton(f"Watermark: {'✅' if settings['watermark'] else '❌'}", callback_data="toggle_watermark")],
        [InlineKeyboardButton(f"Screenshots: {'✅' if settings['screenshots'] else '❌'}", callback_data="toggle_screenshots")],
        [InlineKeyboardButton(f"Demo Clip: {'✅' if settings['demo_clip'] else '❌'}", callback_data="toggle_demo")],
        [InlineKeyboardButton(f"Sprite Sheet: {'✅' if settings['sprite'] else '❌'}", callback_data="toggle_sprite")],
        [InlineKeyboardButton(f"Thumbnail Override: {'✅' if settings['thumbnail_override'] else '❌'}", callback_data="toggle_thumb")]
    ]
    await message.reply("⚙️ Your Settings:", reply_markup=InlineKeyboardMarkup(buttons))