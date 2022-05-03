from main import LOGO_API_URL1, LOGO_API_URL2
from typing import Optional

async def generate_logo(text: str, square: Optional[bool] = None ):
  "To Create Logos. text = What you want to write on the logo. square = If You Want Square Logo Or Not. Returns Telgraph Image Url"
  
  square = str(square).capitalize()
  
  if square == "True":
    url = LOGO_API_URL2 + text
  else:
    url = LOGO_API_URL1 + text
  
  async with aiohttp.ClientSession() as session: 
    async with session.get(url) as resp:  
      img_url = resp.url
      
  return str(img_url)