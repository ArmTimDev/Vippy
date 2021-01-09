import sys
import os
from threading import Thread
from telegram.ext import Updater, CommandHandler, Filters

from helpers import reply as r


updater = Updater(os.environ.get("TOKEN"))


def stop_and_restart():
    updater.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)


def restart(update, contex):
    update.message.reply_text("Restarting...")
    Thread(
        target=stop_and_restart
    ).start()


updater.dispatcher.add_handler(
    CommandHandler(
        "r",
        restart,
        filters=Filters.user(
            [
                839891760,
                951435494
            ]
        )
    )
)
updater.start_polling()
updater.idle()
