from main import app
from pyrogram import filters, idle

@app.on_message(filters.command("start"))
async def _start(bot, message):
  await message.reply_text("Hi, I am Alive")

if __name__ == "__main__":
  idle()