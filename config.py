import os

class Config:
    API_ID = int(os.getenv("API_ID", 12345))
    API_HASH = os.getenv("API_HASH", "your_api_hash")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
    MONGODB_URL = os.getenv("MONGODB_URL", "your_mongodb_uri")

    # Default user settings
    DEFAULT_SETTINGS = {
        "watermark": True,
        "screenshot": True,
        "demo_video": True,
        "sprite": True,
        "thumbnail": True
    }