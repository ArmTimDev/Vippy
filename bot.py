import sys
import os
from threading import Thread
from telegram.ext import Updater, CommandHandler, Filters

from handlers import all_handlers


updater = Updater(os.environ.get("1588959643:AAFLpVH3tELwy2XrrJhf6k8qikKI8gDVFlc"))

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
