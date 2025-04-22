from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from config import Config
from utils import create_welcome_image

app = Client("welcome_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

@app.on_chat_member_updated(filters.group)
async def welcome_handler(_, member: ChatMemberUpdated):
    if member.new_chat_member.user.is_bot or member.old_chat_member.status != "left":
        return

    user = member.new_chat_member.user
    try:
        photos = await app.get_profile_photos(user.id)
        file_id = photos.photos[0].file_id if photos.total_count > 0 else None
        profile_pic_url = None

        if file_id:
            file = await app.download_media(file_id)
            profile_pic_url = file
    except:
        profile_pic_url = None

    image = create_welcome_image(
        name=user.first_name,
        username=f"@{user.username}" if user.username else "N/A",
        user_id=user.id,
        profile_pic_url=profile_pic_url
    )

    await app.send_photo(member.chat.id, image, caption=f"Welcome {user.mention}!")

app.run()