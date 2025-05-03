# main.py
import os
from flask import Flask, request
import requests

TOKEN = "توکنەکەت_لێرە_بخە"
CHAT_ID = "چات_ایدی_لێرە_بخە"
CHANNEL_USERNAME = "@visakurdish"

app = Flask(__name__)

def download_video(url):
    # یەکەم جار ڕاستی پەیوەندیدانی ڤیدیۆ هەبێت (بۆ نموونە بۆ TikTok یان Instagram)
    return "https://some-video-url.com/video.mp4"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            joined = True  # فرض دکەین جوین کردووە - لەراستیدا پێویستە چێک بکرێت
            if not joined:
                send_message(chat_id, f"تکایە یەکەم جار جوین ببە لە {CHANNEL_USERNAME}")
            else:
                send_message(chat_id, "تکایە لینکی ڤیدیوی بێنێ:")
        elif text.startswith("http"):
            video_url = download_video(text)
            send_video(chat_id, video_url)
        else:
            send_message(chat_id, "تکایە لینکی ڤیدیوی بنێرە")

    return {"ok": True}

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

def send_video(chat_id, video_url):
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
    requests.post(url, json={"chat_id": chat_id, "video": video_url})

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(debug=True)