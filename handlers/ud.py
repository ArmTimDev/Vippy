import requests
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async, CommandHandler, Updater


@run_async
def ud(bot: Bot, update: Update):
    message = update.effective_message
    text = message.text[len('/ud '):]
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
