"""
Run this ONCE locally to generate a session string for your Telegram account.
This session string lets GitHub Actions send messages as YOU.

Usage: python generate_session.py
"""
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID = input("Enter your API_ID: ")
API_HASH = input("Enter your API_HASH: ")

with TelegramClient(StringSession(), int(API_ID), API_HASH) as client:
    print("\n\nYour session string (save this as TELEGRAM_SESSION secret):\n")
    print(client.session.save())
