import asyncio
import importlib
import re

from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from main import app
from main.modules import ALL_MODULES
import uvloop

loop = asyncio.get_event_loop()

async def start_bot():
  print("[INFO]:  LOGO MAKER BOT STARTED")
  print("\nJoin @TechZBots")

  await idle()

  await app.stop()
  print("[INFO]: Bye!")
  for task in asyncio.all_tasks():
    task.cancel()
    print("[INFO]: Turned off!")

if __name__ == "__main__":
    uvloop.install()    
    try:
      try:
        loop.run_until_complete(start_bot())
      except asyncio.exceptions.CancelledError:
        pass
      loop.run_until_complete(asyncio.sleep(3.0))
    finally:
      loop.close()