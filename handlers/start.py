from telegram.ext import CommandHandler


def start(update, context):
    update.effective_message.reply_text(
        "Hey there, I'm alive."
    )


__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
