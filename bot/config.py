import os

# دریافت اطلاعات از متغیرهای محیطی
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# هشتگ‌های انگلیسی برای پیدا کردن پست‌های وایرال
HASHTAGS = [
    "funnyreels", "funnymemes", "comedyvideos", "hilarious",
    "funnyclips", "dailyhumor", "relatablememes", "viralvideos",
    "lol", "memestagram"
]

# پوشه ذخیره ویدیوها
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
