import os
from threading import Thread
from flask import Flask
from telethon import TelegramClient, events, Button

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!"

def run():
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

API_ID = int(os.getenv("API_ID", "28013497"))
API_HASH = os.getenv("API_HASH", "3bd0587beedb80c8336bdea42fc67e27")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7045596311:AAH7tHcSt16thbFpL0JsVNSEHBvKtjnK8sk")


if not all([API_ID, API_HASH, BOT_TOKEN]):
    print("Error: Missing API_ID, API_HASH or BOT_TOKEN environment variable.")
    exit(1)

keep_alive()

bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern="(?i).*"))
async def handler(event):
    try:
        buttons = [
            [Button.inline("Button 1", b"btn1"), Button.inline("Button 2", b"btn2")]
        ]
        await event.reply(
            "សួស្តី 😄 នេះគឺជាប៊ូតុង 2 បញ្ចូលជាមួយសាររបស់ខ្ញុំ!",
            buttons=buttons
        )
    except Exception as e:
        print(f"Error replying to user {event.sender_id}: {e}")

@bot.on(events.CallbackQuery)
async def callback_handler(event):
    data = event.data.decode('utf-8')
    if data == "btn1":
        await event.answer("អ្នកចុច Button 1")
    elif data == "btn2":
        await event.answer("អ្នកចុច Button 2")
    else:
        await event.answer("Unknown button")

print("Bot started and web server is running...")

bot.run_until_disconnected()
