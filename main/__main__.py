from main import app
from pyrogram import filters, idle
from main.logo import generate_logo

HELP =
@app.on_message(filters.command("start"))
async def _start(bot, message):
  await message.reply_text("Hi, I am Alive")

@app.on_message(filters.command("logo") | filters.regex("logo"))
async def logo(bot, message):
  text = message.text.replace("logo","").replace("/logo","").replace("@TechZLogoMakerBot").strip().upper()
  
  if text == "":
    return await message.reply_text(HELP)
  x = await message.reply_text("`🔍 Generating Logo For You...`")
  
  logo = await generate_logo()

if __name__ == "__main__":
  idle()
