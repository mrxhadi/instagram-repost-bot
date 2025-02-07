import multiprocessing
import os

def run_scheduler():
    os.system("python bot/scheduler.py")

def run_telegram_bot():
    os.system("python bot/telegram_bot.py")

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=run_scheduler)
    process2 = multiprocessing.Process(target=run_telegram_bot)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
