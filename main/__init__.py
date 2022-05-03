import asyncio
from inspect import getfullargspec
from pyrogram import Client
from pyrogram.types import Message
from config import *

loop = asyncio.get_event_loop()

app = Client("main", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

print("[INFO]: STARTING BOT CLIENT")
app.start()