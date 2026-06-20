import os
import time
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send(msg):
    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

if __name__ == "__main__":
    send("재입고 감시기가 정상적으로 시작되었습니다.")
    
    while True:
        time.sleep(3600)
