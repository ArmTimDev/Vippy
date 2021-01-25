from telegram.ext import CommandHandler


def start(update, context):
    update.effective_message.reply_text(
        "✋ Hello !\n🧠 I'm An Ai !\n❤ Made With Love By @BotLoversOfficial Team !"
    )


__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
