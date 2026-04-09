import os
import asyncio
from datetime import datetime
import pytz
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.environ["TELEGRAM_API_ID"])
API_HASH = os.environ["TELEGRAM_API_HASH"]
SESSION_STRING = os.environ["TELEGRAM_SESSION"]
# Comma-separated group usernames e.g. "@group1,@group2"
CHAT_IDS = os.environ["TELEGRAM_CHAT_IDS"].split(",")
MESSAGE = os.environ.get("TELEGRAM_MESSAGE", "Hello from OA Support HUB!").replace("\\n", "\n")

TIMEZONE = pytz.timezone("Asia/Kolkata")


async def send_messages():
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.connect()

    now = datetime.now(TIMEZONE).strftime('%Y-%m-%d %H:%M:%S IST')

    for chat_id in CHAT_IDS:
        chat_id = chat_id.strip()
        try:
            await client.send_message(chat_id, MESSAGE)
            print(f"[OK] Sent to {chat_id} at {now}")
        except Exception as e:
            print(f"[FAIL] Could not send to {chat_id}: {e}")
        await asyncio.sleep(2)

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(send_messages())
