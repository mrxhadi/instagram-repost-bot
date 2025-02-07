import yt_dlp
import os
import random
import time
from config import HASHTAGS, DOWNLOAD_FOLDER

# شبیه‌سازی لینک‌های پست وایرال (در عمل باید از اینستاگرام دریافت شود)
video_urls = [
    f"https://www.instagram.com/explore/tags/{random.choice(HASHTAGS)}/"
]

def download_instagram_reel():
    video_url = random.choice(video_urls)

    # ایجاد وقفه تصادفی بین 10 تا 30 ثانیه برای جلوگیری از بلاک شدن
    sleep_time = random.randint(10, 30)
    print(f"⏳ در انتظار {sleep_time} ثانیه برای جلوگیری از بلاک شدن...")
    time.sleep(sleep_time)

    ydl_opts = {
        'outtmpl': f"{DOWNLOAD_FOLDER}/%(id)s.%(ext)s",
        'format': 'bestvideo+bestaudio/best',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_url, download=True)
            return info['id'], info['ext']
        except Exception as e:
            print(f"⚠️ خطا در دانلود: {e}")
            return None, None

# دانلود یک ریلز تصادفی بر اساس هشتگ‌های جدید
video_id, video_ext = download_instagram_reel()
if video_id:
    downloaded_video = f"{DOWNLOAD_FOLDER}/{video_id}.{video_ext}"
    print(f"✅ ویدیو دانلود شد: {downloaded_video}")
else:
    print("❌ دانلود ویدیو با مشکل مواجه شد.")
