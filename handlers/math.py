import math

import pynewtonmath as newton
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def math(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    message.reply_text(newton.simplify('{}'.format(args[0])))

__handlers__ = [
    [
        CommandHandler(
            "math",
            math
        )
    ]
]
