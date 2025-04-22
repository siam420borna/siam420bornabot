from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from config import Config

def create_welcome_image(name, username, user_id, profile_pic_path=None):
    base = Image.new("RGB", (1280, 720), "#0f0f0f")
    draw = ImageDraw.Draw(base)

    font_big = ImageFont.truetype("arialbd.ttf", 80)
    font_small = ImageFont.truetype("arialbd.ttf", 45)

    draw.text((60, 100), "WELCOME", fill="#ffaa00", font=font_big)
    draw.text((60, 250), f"NAME :  {name}", fill="#ffffff", font=font_small)
    draw.text((60, 330), f"USERNAME :  {username}", fill="#ffffff", font=font_small)
    draw.text((60, 410), f"USER ID :  {user_id}", fill="#ffffff", font=font_small)

    try:
        pf = Image.open(profile_pic_path or Config.DEFAULT_IMG).resize((300, 300)).convert("RGBA")
    except:
        pf = Image.open(Config.DEFAULT_IMG).resize((300, 300)).convert("RGBA")

    base.paste(pf, (900, 200))
    output = BytesIO()
    output.name = "welcome.jpg"
    base.save(output, "JPEG")
    output.seek(0)
    return output