from PIL import Image, ImageDraw, ImageFont
import requests

def create_welcome_image(photo_path, name, username, user_id):
    base = Image.open("default.jpg").convert("RGBA")
    avatar = Image.open(photo_path).resize((150, 150)).convert("RGBA")

    base.paste(avatar, (30, 30), avatar)

    draw = ImageDraw.Draw(base)
    font = ImageFont.truetype("arial.ttf", 24)

    draw.text((200, 50), f"Name: {name}", font=font, fill="white")
    draw.text((200, 90), f"Username: @{username if username else 'N/A'}", font=font, fill="white")
    draw.text((200, 130), f"User ID: {user_id}", font=font, fill="white")

    output_path = f"welcome_{user_id}.png"
    base.save(output_path)
    return output_path