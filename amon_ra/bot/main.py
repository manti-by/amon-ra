import logging.config

from telegram.ext import ApplicationBuilder, CommandHandler

from amon_ra.bot.settings import BOT_TOKEN, LOGGING
from amon_ra.bot.services.telegram import start

logging.config.dictConfig(LOGGING)


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
