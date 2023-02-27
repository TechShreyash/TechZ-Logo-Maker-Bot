import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = ""
API_HASH = ""

# Get it from @Botfather in Telegram.
BOT_TOKEN = ""

# Create Your Own ApiKey From @TechZApiBot To Use Logo Api
API_KEY = ""


# Don't Change Anything Below This Line


if not API_ID or API_ID.strip() == "":
    API_ID = int(getenv("API_ID"))
if not API_HASH or API_HASH.strip() == "":
    API_HASH = getenv("API_HASH")
if not BOT_TOKEN or BOT_TOKEN.strip() == "":
    BOT_TOKEN = getenv("BOT_TOKEN")
if not API_KEY or API_KEY.strip() == "":
    API_KEY = getenv("API_KEY")


LOGO_API_URL1 = f"https://techzapi.azurewebsites.net/logo?api_key={API_KEY}&text="

LOGO_API_URL2 = (
    f"https://techzapi.azurewebsites.net//logo?api_key={API_KEY}&square=True&text="
)


if not API_KEY:
    print("Error: API_KEY Not Found!")
    print("Please Get Your Own ApiKey From @TechZApiBot To Use Logo Api")
    sys.exit()
elif API_KEY.strip() == "":
    print("Error: API_KEY Not Found!")
    print("Please Get Your Own ApiKey From @TechZApiBot To Use Logo Api")
    sys.exit()
