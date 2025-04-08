import requests
import schedule
import time

BOT_TOKEN = '8040847687:AAGCjt-3q82sD0NNjahIFmEeNHaN1XOzbDY'
CHAT_ID = '7289034982'

def send_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

def push_morning():
    send_message("早安！這是 8:30 的推播訊息。")

def push_noon():
    send_message("午安！這是 12:00 的策略更新。")

def push_afternoon():
    send_message("下午好！這是 15:00 的即時快訊。")

def push_night():
    send_message("晚上好！這是 21:30 的盤後分析。")

schedule.every().day.at("08:30").do(push_morning)
schedule.every().day.at("12:00").do(push_noon)
schedule.every().day.at("15:00").do(push_afternoon)
schedule.every().day.at("21:30").do(push_night)

while True:
    schedule.run_pending()
    time.sleep(1)
