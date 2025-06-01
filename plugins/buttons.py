from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_buttons(info):
    buttons = []
    for f in info.get("formats", []):
        label = f"{f['format_note']} - {f['ext']} - {f['filesize_mb']}MB"
        buttons.append([InlineKeyboardButton(label, callback_data=f"download_{f['format_id']}")])
    return InlineKeyboardMarkup(buttons)