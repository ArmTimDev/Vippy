from telegram import Update
from telegram.ext import Updater, CommandHandler

def stb(update, context):
  str = update.message.text.replace(update.message.text.split(' ')[0], '')
  update.effective_message.reply_text(
    "Binary : \n\n", ' '.join(format(x, 'b') for x in bytearray(str, 'utf-8'))
    )
  
__handlers__ = [
    [
        CommandHandler(
            "stb",
            stb
        )
    ]
]
