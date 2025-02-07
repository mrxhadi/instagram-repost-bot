import telebot
import os

# دریافت متغیرهای محیطی
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

bot = telebot.TeleBot(TOKEN)

# دریافت وضعیت ربات
@bot.message_handler(commands=['status'])
def check_status(message):
    if str(message.chat.id) != ADMIN_CHAT_ID:
        return
    bot.reply_to(message, "✅ ربات فعال است و در حال اجرا.")

# دانلود یک پست وایرال و ارسال لینک آن
@bot.message_handler(commands=['getpost'])
def get_viral_post(message):
    if str(message.chat.id) != ADMIN_CHAT_ID:
        return
    bot.reply_to(message, "🔍 در حال جستجو برای یک پست وایرال...")
    
    import downloader
    video_id, video_ext = downloader.download_instagram_reel()
    video_path = f"downloads/{video_id}.{video_ext}"
    
    if os.path.exists(video_path):
        bot.reply_to(message, f"✅ ویدیو دانلود شد!
مسیر: {video_path}")
    else:
        bot.reply_to(message, "⚠️ مشکلی در دانلود ویدیو به وجود آمد.")

# آپلود ویدیو از تلگرام به اینستاگرام
@bot.message_handler(content_types=['video'])
def handle_video(message):
    if str(message.chat.id) != ADMIN_CHAT_ID:
        return
    bot.reply_to(message, "📥 در حال دریافت ویدیو...")
    
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    video_path = f"downloads/manual_upload.mp4"
    with open(video_path, "wb") as new_file:
        new_file.write(downloaded_file)
    
    bot.reply_to(message, "✅ ویدیو دریافت شد! در حال ارسال به اینستاگرام...")
    
    import uploader
    uploader.upload_to_instagram(video_path)
    
    bot.reply_to(message, "✅ ویدیو در اینستاگرام آپلود شد!")

# تنظیم زمان ارسال پست روزانه
@bot.message_handler(commands=['settime'])
def set_post_time(message):
    if str(message.chat.id) != ADMIN_CHAT_ID:
        return
    try:
        time_str = message.text.split()[1]
        with open("schedule_time.txt", "w") as f:
            f.write(time_str)
        bot.reply_to(message, f"✅ زمان ارسال پست تنظیم شد: {time_str}")
    except:
        bot.reply_to(message, "⚠️ فرمت صحیح: /settime HH:MM")

# شروع و متوقف کردن ربات
@bot.message_handler(commands=['start', 'stop'])
def control_bot(message):
    if str(message.chat.id) != ADMIN_CHAT_ID:
        return
    command = "scheduler.py"
    if message.text == "/start":
        os.system(f"python {command} &")
        bot.reply_to(message, "✅ ربات راه‌اندازی شد!")
    elif message.text == "/stop":
        os.system(f"pkill -f {command}")
        bot.reply_to(message, "⛔ ربات متوقف شد!")

bot.polling(none_stop=True)
