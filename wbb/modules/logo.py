from pyrogram import filters
from main import app

@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_text("i am up")