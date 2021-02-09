from telegram.ext import CommandHandler


def start(update, context):
    update.effective_message.reply_text(
        "✋ Hello !\n I'm Vippy Ai Bot\n 🧠 I am Also known as chatbot I !\n❤ Made With Love By @VippyNews Team !\n Head to @VippyDiscussion\n ⚠️ NOTE : My AI Will only work on Groups.
    )


__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
