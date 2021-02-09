from telegram.ext import CommandHandler


def start(update, context):
    update.effective_message.reply_text(
        "✋ Hello !\n\n⚀ I'm An Ai !\n❤ Made With Love By @VippyNews Team !\n⚠️ Note : My Ai Will Work Only In Groups !"
    )


__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
