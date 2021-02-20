from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from gtts import gTTS
import os

language = 'en'
def stts(update: Update, context: CallbackContext) -> None:
 tts = update.message.text.replace(update.message.text.split(' ')[0], '')
 myobj = gTTS(text=tts, lang=language, slow=True)
 file_id = str(update.message.from_user.id) + '.mp3'
 myobj.save(file_id)
 context.bot.sendAudio(chat_id=update.message.chat.id, audio=open(file_id, 'rb'), title='Vippy TTS')
 os.remove(file_id)

__handlers__ = [
    [
        CommandHandler(
            "stts",
            stts
        )
    ]
]
