import random
from telegram.ext import CommandHandler

msg = ["Hi ! I'm Always Here !", "Hello ? Anyone Here ?", "I'm Online !"]

def start(update, context):
    update.effective_message.reply_text(
        random.choice(msg)
    )


__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
