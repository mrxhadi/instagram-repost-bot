import schedule
import time
import os
from downloader import download_instagram_reel
from uploader import upload_to_instagram

# تابعی برای خواندن زمان از فایل
def read_schedule_time():
    try:
        with open("schedule_time.txt", "r") as f:
            return f.read().strip()
    except:
        return "19:00"  # مقدار پیش‌فرض

def job():
    print("🔍 در حال دانلود پست وایرال...")
    video_id, video_ext = download_instagram_reel()
    video_path = f"downloads/{video_id}.{video_ext}"
    
    caption = "🔥 Viral funny reel of the day! 

#funnyreels #funnymemes #comedyvideos"
    
    print("📤 در حال ارسال پست...")
    upload_to_instagram(video_path, caption)

# تنظیم زمان اجرای خودکار
POST_TIME = read_schedule_time()
schedule.every().day.at(POST_TIME).do(job)

print(f"✅ ربات آماده است. پست‌ها هر روز ساعت {POST_TIME} ارسال خواهند شد.")

while True:
    schedule.run_pending()
    time.sleep(60)
