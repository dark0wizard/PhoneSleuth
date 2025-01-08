import httpx
import random
from core.settings import ua, split_phone_number
from ignorant.modules.shopping.amazon import amazon
from ignorant.modules.social_media.instagram import instagram

# The original repository: https://github.com/megadose/ignorant


async def amazon_insta(phone):
    country_code, remaining_number = split_phone_number(phone)
    user_agent = {'User-Agent': random.choice(ua)}
    client = httpx.AsyncClient(headers=user_agent)
    out = []
    data = {}
    await instagram(remaining_number, country_code, client, out)
    await amazon(remaining_number, country_code, client, out)
    for i in out:
        data.update({i['name']: i})
    await client.aclose()
    return False if len(data) == 0 else data

