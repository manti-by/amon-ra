import aiohttp
from telegram import Chat, Message

from amon_ra.apps.core.services import get_data_hash
from ..settings import DJANGO_HOST, APP_KEY, APP_HASH


async def add_data_hash(data: dict) -> dict:
    data["key"] = APP_KEY
    return {**data, "hash": get_data_hash(data=data, secret_key=APP_HASH)}


async def get_user(chat: Chat) -> dict:
    data = await add_data_hash({"chat_id": chat.id})
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{DJANGO_HOST}/api/v1/subscription/", data=data) as response:
            if response.ok:
                return await response.json()


async def link_user(chat: Chat, message: Message) -> bool:
    data = await add_data_hash(
        {
            "email": message.text,
            "chat_id": chat.id,
            "username": chat.username,
            "first_name": chat.first_name,
            "last_name": chat.last_name,
        }
    )
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{DJANGO_HOST}/api/v1/subscription/link/", data=data) as response:
            return response.ok


async def unlink_user(chat: Chat) -> bool:
    data = await add_data_hash({"chat_id": chat.id})
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{DJANGO_HOST}/api/v1/subscription/unlink/", data=data) as response:
            return response.ok
