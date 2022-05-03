from pyrogram import Client
from config import *
import aiohttp

app = Client(
  "bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

print("STARTING BOT...")
app.start()

print("Creating Aiohttp Session...")
ses = aiohttp.ClientSession()