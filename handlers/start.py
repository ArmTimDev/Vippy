from telegram.ext import CommandHandler, Updater

def start(update, context):
    update.effective_message.reply_text(
        "✋ Hello !\n\n⚀ I'm An Ai !\n❤ Made With Love By @VippyNews Team !"
    )
    print("New User ! \nUser ID : " + str(update.message.from_user.id) + "\nUser Name : " + str(update.message.from_user.username))
    

__handlers__ = [
    [
        CommandHandler(
            "start",
            start
        )
    ]
]
