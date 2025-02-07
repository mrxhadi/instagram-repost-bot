import os

# دریافت اطلاعات از متغیرهای محیطی
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = str(os.getenv("ADMIN_CHAT_ID"))

# هشتگ‌های انگلیسی برای پیدا کردن پست‌های وایرال
HASHTAGS = [
    "funnyreels", "funnymemes", "comedyvideos", "hilarious",
    "funnyclips", "dailyhumor", "relatablememes", "viralvideos",
    "lol", "memestagram"
]

# پوشه ذخیره ویدیوها
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
