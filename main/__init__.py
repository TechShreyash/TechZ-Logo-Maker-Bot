from pyrogram import Client
from config import *

app = Client(
  "bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=TOKEN
)

print("STARTING BOT")
app.start()
