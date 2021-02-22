from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from gtts import gTTS
import os


language = 'en'
def tts(update: Update, context: CallbackContext) -> None:
 context.bot.send_chat_action(update.effective_chat.id, "record_audio")
 tts = update.message.text.replace(update.message.text.split(' ')[0], '')
 myobj = gTTS(text=tts, lang=language, slow=False)
 file_id = str(update.message.from_user.id) + '.mp3'
 myobj.save(file_id)
 context.bot.sendAudio(chat_id=update.message.chat.id, audio=open(file_id, 'rb'), title='Vippy TTS')
 os.remove(file_id)

__handlers__ = [
    [
        CommandHandler(
            "tts",
            tts
        )
    ]
]
