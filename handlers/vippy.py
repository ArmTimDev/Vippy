import random
from telegram.ext import CommandHandler

msg = ["Hi ! I'm Always Here !", "Hello ? Anyone Here ?", "I'm Online !"]

def vippy(update, context):
    update.effective_message.reply_text(
        random.choice(msg)
    )


__handlers__ = [
    [
        CommandHandler(
            "vippy",
            vippy
        )
    ]
]
