from telegram.ext import MessageHandler, Filters
from helpers import reply as r


def reply(update, context):
    try:
        context.bot.send_chat_action(update.effective_chat.id, "typing")
        update.effective_message.reply_text(
            r(
                update.effective_message.text
            )
        )
    except:
        pass


__handlers__ = [
    [
        MessageHandler(
            Filters.text & Filters.reply,
            reply
        )
    ]
]
