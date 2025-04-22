from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from config import Config
from utils import create_welcome_image
import os

app = Client("welcome_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@app.on_chat_member_updated(filters.group)
async def welcome_handler(_, member: ChatMemberUpdated):
    if member.new_chat_member.user.is_bot or member.old_chat_member.status != "left":
        return

    user = member.new_chat_member.user
    profile_pic_path = None

    try:
        photos = await app.get_profile_photos(user.id)
        if photos.total_count > 0:
            profile_pic_path = await app.download_media(photos.photos[0].file_id)
    except:
        profile_pic_path = None

    image = create_welcome_image(
        name=user.first_name,
        username=f"@{user.username}" if user.username else "N/A",
        user_id=user.id,
        profile_pic_path=profile_pic_path  # লোকাল পাথ পাঠাচ্ছি
    )

    await app.send_photo(member.chat.id, image, caption=f"Welcome {user.mention}!")

    # অস্থায়ী ইমেজ ফাইল ডিলিট
    if profile_pic_path and os.path.exists(profile_pic_path):
        os.remove(profile_pic_path)

app.run()