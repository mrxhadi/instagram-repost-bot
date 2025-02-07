import yt_dlp
import os
import random
from config import HASHTAGS, DOWNLOAD_FOLDER

# شبیه‌سازی لینک‌های پست وایرال (در عمل باید از اینستاگرام دریافت شود)
video_urls = [
    f"https://www.instagram.com/explore/tags/{random.choice(HASHTAGS)}/"
]

def download_instagram_reel(video_url):
    ydl_opts = {
        'outtmpl': f"{DOWNLOAD_FOLDER}/%(id)s.%(ext)s",
        'format': 'bestvideo+bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        return info['id'], info['ext']

# دانلود یک ریلز تصادفی بر اساس هشتگ‌های جدید
video_id, video_ext = download_instagram_reel(random.choice(video_urls))
downloaded_video = f"{DOWNLOAD_FOLDER}/{video_id}.{video_ext}"

print("✅ ویدیو دانلود شد:", downloaded_video)
