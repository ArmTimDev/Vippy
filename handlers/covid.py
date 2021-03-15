from telegram.ext import CommandHandler, Updater
#from covid19_data import JHU

def covid(update, context):
  update.effective_message.reply_text(
        "😷 Wear A Mask\n👋 Wash Your Hands Often\n🤧 Cover Your Coughs And Sneezes\n\nBut sorry I can not display stats due to the problems, I will continue showing them soon :D"
    )
    
    
__handlers__ = [
    [
        CommandHandler(
            "covid",
            covid
        )
    ]
]
