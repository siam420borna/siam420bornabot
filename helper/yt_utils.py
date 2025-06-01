import yt_dlp
import asyncio

async def extract_info(url):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, lambda: _extract(url))

def _extract(url):
    ydl_opts = {
        'quiet': True,
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        for f in info.get("formats", []):
            if f.get("filesize"):
                f["filesize_mb"] = round(f["filesize"] / 1024 / 1024, 2)
        return info