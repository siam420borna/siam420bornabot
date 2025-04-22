from PIL import Image, ImageDraw, ImageFont
from pyrogram.types import User
import requests
from io import BytesIO

async def create_welcome_image(user: User):
    try:
        if user.photo:
            photo = await user.get_profile_photos(limit=1)
            file = await photo[0].get_file()
            response = await file.download()
            pfp = Image.open(response).convert("RGBA")
        else:
            raise Exception("No photo")
    except:
        pfp = Image.open("default.jpg").convert("RGBA")

    base = Image.new("RGBA", (800, 400), "white")
    pfp = pfp.resize((200, 200))
    base.paste(pfp, (50, 100))

    draw = ImageDraw.Draw(base)
    font = ImageFont.truetype("arial.ttf", size=40)

    draw.text((270, 120), f"Welcome {user.first_name}", fill="black", font=font)
    draw.text((270, 180), f"@{user.username or 'No Username'}", fill="gray", font=font)
    draw.text((270, 240), f"User ID: {user.id}", fill="blue", font=font)

    output = BytesIO()
    base.save(output, format="PNG")
    output.seek(0)
    return output