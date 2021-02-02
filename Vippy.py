import sys
import os
from threading import Thread
from telegram.ext import Updater, CommandHandler, Filters

from handlers import all_handlers

A = Config.TG_BOT_TOKEN

updater = Updater(A)

for handler in all_handlers:
    if len(handler) == 2:
        updater.dispatcher.add_handler(
            handler[0],
            handler[1]
        )
    else:
        updater.dispatcher.add_handler(
            handler[0]
        )


def stop_and_restart():
    updater.stop()
    os.system("git pull")
    os.execl(sys.executable, sys.executable, *sys.argv)


def restart(update, contex):
    update.message.reply_text("Restarting Vippy...")
    Thread(
        target=stop_and_restart
    ).start()


updater.dispatcher.add_handler(
    CommandHandler(
        "restart",
        restart,
        filters=Filters.user(
            [
                #Sudo Users User ID
            ]
        )
    )
)
updater.start_polling()
updater.idle()
