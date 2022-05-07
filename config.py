from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# API By TechZBots || https://t.me/TechZBots
WALL_API = "https://techzbotsapi.herokuapp.com/wall?query="

UNSPLASH_API = "https://techzbotsapi.herokuapp.com/unsplash?query="