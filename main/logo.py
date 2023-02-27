from main import LOGO_API_URL1, LOGO_API_URL2, session
from typing import Optional
import aiohttp
from string import ascii_letters, digits
import random


async def generate_logo(text: str, square: Optional[bool] = False):
    "To Create Logos. text = What you want to write on the logo. square = If You Want Square Logo Or Not. Returns Telgraph Image Url"

    try:
        square = str(square).capitalize()

        if square == "True":
            url = LOGO_API_URL2 + text
        else:
            url = LOGO_API_URL1 + text

        resp = await session.get(url)
        img = "".join(random.choices(ascii_letters + digits, k=10)) + ".jpg"
        with open(img, "wb") as f:
            f.write(await resp.read())
    except Exception as e:
        print("error" + str(e))
        return "error" + str(e)
    return img
