import aiohttp
from amon_ra.bot.settings import DJANGO_HOST


async def get_user(chat_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{DJANGO_HOST}/api/v1/bot/user/{chat_id}/") as response:
            return await response.json()
