from telegram import Bot, Message

from ..settings import BOT_TOKEN


async def send_message(chat_id: int, text: str, *args, **kwargs) -> Message:
    bot = Bot(BOT_TOKEN)
    return await bot.send_message(*args, chat_id=chat_id, text=text, **kwargs)
