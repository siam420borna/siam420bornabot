from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

client = AsyncIOMotorClient(Config.MONGODB_URL)
db = client.videobot
settings_col = db.settings

def default_settings():
    return {
        "watermark": False,
        "screenshots": False,
        "demo_clip": False,
        "sprite": False,
        "thumbnail_override": False
    }

async def get_user_settings(user_id):
    data = await settings_col.find_one({"user_id": user_id})
    if not data:
        await settings_col.insert_one({"user_id": user_id, **default_settings()})
        return default_settings()
    return {k: data.get(k, False) for k in default_settings().keys()}

async def toggle_user_setting(user_id, setting):
    current = await get_user_settings(user_id)
    new_value = not current.get(setting, False)
    await settings_col.update_one({"user_id": user_id}, {"$set": {setting: new_value}}, upsert=True)
