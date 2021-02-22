from telegram.ext import CommandHandler, Updater
from covid19_data import JHU

def covid(update, context):
  update.effective_message.reply_text(
        "🦠 COVID-19 Stats 🦠\n\n🌐 The Number Of Worldwide COVID-19 Recovered : " + str(JHU.Total.recovered) + "\n🌐 The Number Of Worldwide COVID-19 Confirmed : " + str(JHU.Total.confirmed) + "\n🌐 The Number Of Worldwide COVID-19 Deaths : " + str(JHU.Total.deaths) + "\n\n😷 Wear A Mask\n👋 Wash Your Hands Often\n🤧 Cover Your Coughs And Sneezes"
    )
    
    
__handlers__ = [
    [
        CommandHandler(
            "covid",
            covid
        )
    ]
]
