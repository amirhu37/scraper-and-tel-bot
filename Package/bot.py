
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import  ReplyKeyboardRemove
import telegram
import logging
import os


TOKEN = ''

logger = logging.getLogger(__name__)

bot = telegram.Bot(token=TOKEN)

PORT = int(os.environ.get('PORT', 80))

CHAT_ID = ''

WEB_HOOK = ''

SEND , RECEIVE = range(2)

def send(update):
    f = open('res.txt','r')
    txt = ''.join(f.readlines())
    update.message.reply_text(txt) #f.readlines()[0]
    f.close()
    return SEND

def cancel(update):
    user = update.message.from_user
    logger.info("User %s canceled the coneversation", user.first_name)

    update.message.reply_text(
        'Maybe Next Time', reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END



def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('last', send)],

        states={
            SEND : [MessageHandler(Filters.text, send)]
        },

        fallbacks=[CommandHandler('cancle', cancel)]
    )

    dp.add_handler(conv_handler)
    updater.start_webhook(listen='0.0.0.0', port=PORT,
                          url_path=TOKEN, webhook_url=f'{WEB_HOOK}/{TOKEN}')
    updater.start_polling(timeout=600)
    updater.idle()


