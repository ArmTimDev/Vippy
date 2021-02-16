from telegram.ext import MessageHandler, Filters, CallbackContext
from helpers import reply as r
from gtts import gTTS


def tts(update: Update, context: CallbackContext) -> None:
    tts = update.effective_message.reply_text
    myobj = gTTS(text=tts, lang=language, slow=False)
    file_id = str(update.message.from_user.id) + '.mp3'
    myobj.save(file_id)
    context.bot.sendAudio(chat_id=update.message.chat.id, audio=open(file_id, 'rb'), title='Answer')
    os.remove(file_id)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("tts", tts))
