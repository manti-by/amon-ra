import logging.config

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from amon_ra.bot.settings import BOT_TOKEN, LOGGING
from amon_ra.bot.services.telegram import post_init, start, link, unlink, message

logging.config.dictConfig(LOGGING)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("link", link))
    app.add_handler(CommandHandler("unlink", unlink))
    app.add_handler(MessageHandler(~filters.COMMAND, message))
    app.run_polling()
