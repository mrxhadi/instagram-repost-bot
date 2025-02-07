from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from config import USERNAME, PASSWORD, HASHTAGS

def upload_to_instagram(video_path):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # اجرای بدون UI
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # تنظیم User-Agent برای جلوگیری از بلاک شدن
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    service = Service("/usr/local/bin/chromedriver")  # مسیر در Railway
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get("https://www.instagram.com/")
        time.sleep(5)

        # ورود به اینستاگرام
        driver.find_element(By.NAME, "username").send_keys(USERNAME)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(10)

        # رفتن به صفحه ارسال پست
        driver.get("https://www.instagram.com/create/style/")
        time.sleep(5)

        # آپلود ویدیو
        upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_input.send_keys(os.path.abspath(video_path))
        time.sleep(10)

        # ساخت کپشن با هشتگ‌های جدید
        caption = f"🔥 Viral funny reel of the day!\n\n{' '.join(['#' + tag for tag in HASHTAGS])}"
        caption_box = driver.find_element(By.XPATH, "//textarea")
        caption_box.send_keys(caption)

        time.sleep(3)

        # ارسال پست
        share_button = driver.find_element(By.XPATH, "//button[text()='Share']")
        share_button.click()

        print("✅ پست ارسال شد!")
        time.sleep(10)

    except Exception as e:
        print(f"❌ خطا در آپلود: {e}")

    finally:
        driver.quit()

# تست آپلود
if __name__ == "__main__":
    video_path = "downloads/sample.mp4"  # مسیر ویدیو برای تست
    upload_to_instagram(video_path)
