from telegram import BotCommand, Update
from telegram.ext import Application, ContextTypes

from ..services.django import get_user, link_user, unlink_user


async def post_init(application: Application) -> None:
    bot = application.bot
    await bot.set_my_commands(
        commands=(
            BotCommand("start", "Start"),
            BotCommand("link", "Link Account"),
            BotCommand("unlink", "Unlink Account"),
        )
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = await get_user(update.effective_chat)
    if not response:
        await update.message.reply_text(
            "Hi, I'm Amon-Ra bot. You can link your account on Amon-Ra portal with me.\n"
            "Use /link command to link your account."
        )
        return
    await update.message.reply_text(
        "Your account has already linked on Amon-Ra portal.\n" "Use /unlink command to unlink your account."
    )


async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = await get_user(update.effective_chat)
    if not response:
        await update.message.reply_text("Enter email to link your account:")
        return
    await update.message.reply_text("Your account has already linked on Amon-Ra portal!")


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = await link_user(update.effective_chat, update.message)
    if not response:
        await update.message.reply_text("Something goes wrong, please try again later.")
        return
    await update.message.reply_text("Your account have successfully linked on Amon-Ra portal.")


async def unlink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = await unlink_user(update.effective_chat)
    if not response:
        await update.message.reply_text("Something goes wrong, please try again later.")
        return
    await update.message.reply_text("Your account have successfully unlinked on Amon-Ra portal.")
