from telegram.ext import CommandHandler, Updater

def start(update, context):
    update.effective_message.reply_text(
        "✋ Hello !\n\n⚀ I'm An Ai !\n❤ Made With Love By @VippyNews Team !"
    )
    user_id = str(update.message.from_user.id)
    A = open("users.txt", "a")
    A.write(user_id)
    A.close()
    

__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
