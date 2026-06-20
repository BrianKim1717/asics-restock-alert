import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

MODEL = "1201A438-001"

MUSINSA_URL = "https://www.musinsa.com/search/goods?keyword=1201A438-001&gf=A&keywordType=keyword&isSoldOut=true"
ASICS_URL = "https://www.asics.co.kr/p/AKR_112519319-001"

def send(msg):
requests.get(
f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
params={
"chat_id": CHAT_ID,
"text": msg
},
timeout=20
)

def check_url(url):
try:
r = requests.get(
url,
headers={
"User-Agent": "Mozilla/5.0"
},
timeout=20
)
return r.status_code, r.text
except Exception as e:
return None, str(e)

musinsa_status, musinsa_html = check_url(MUSINSA_URL)
asics_status, asics_html = check_url(ASICS_URL)

message = f"""재고 감시 실행

모델: {MODEL}

MUSINSA 상태: {musinsa_status}
ASICS 상태: {asics_status}
"""

send(message)
