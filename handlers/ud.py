import requests
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async, CommandHandler, Updater


@run_async
def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    text = update.message.text.replace(update.message.text.split(' ')[0], '')
    results = requests.get(f'http://api.urbandictionary.com/v0/define?term={text}').json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No Results Found ! Try Another Word !"
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)
    
__handlers__ = [
    [
        CommandHandler(
            "ud",
            ud
        )
    ]
]
