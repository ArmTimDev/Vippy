from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from helpers import reply as r


def start(update, context):
    update.effective_message.reply_text(
        "Hey there, I'm alive."
    )


def reply(update, context):
    try:
        update.effective_message.reply_text(
            r(
                update.effective_message.text
            )
        )
    except:
        pass


updater = Updater("TOKEN")
updater.dispatcher.add_handler(
    MessageHandler(
        Filters.text & Filters.chat_type.groups,
        reply
    )
)
updater.dispatcher.add_handler(
    CommandHandler(
        "start", start
    )
)
updater.start_polling()
updater.idle()
