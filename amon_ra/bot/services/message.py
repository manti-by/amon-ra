from ..settings import BOT_TOKEN

from telegram import Bot, Message


async def send_message(chat_id: int, text: str) -> Message:
    bot = Bot(BOT_TOKEN)
    return await bot.send_message(chat_id=chat_id, text=text)
