from telegram import Update
from telegram.ext import ContextTypes

from amon_ra.bot.services.django import get_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = await get_user(update.effective_chat.id)
    if not response["is_linked"]:
        await update.message.reply_text("Please link you account on Amon-Ra portal")
        return
    await update.message.reply_text("Your account has already linked on Amon-Ra portal")
