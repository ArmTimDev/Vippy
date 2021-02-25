from telegram import Update
from telegram.ext import Updater, CommandHandler

def stb(update, context):
  str = update.message.text.replace(update.message.text.split(' ')[0], '')
  bin = ''.join(format(i, '08b') for i in bytearray(str, encoding ='utf-8')) 
  update.effective_message.reply_text(
    "Binary : \n\n", str(bin)
    )
  
__handlers__ = [
    [
        CommandHandler(
            "stb",
            stb
        )
    ]
]
