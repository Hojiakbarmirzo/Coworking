from telegram.ext import Updater
updater = Updater(token='1770875004:AAGyA9bzuZb2DLaS7X9xr-Pi7qtXfIdzhbc', use_context=True)
def start(update, context):
    context.bot.send_message(chat_id=1051394478, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
updater.start_polling()
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=1051394478, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)
from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)