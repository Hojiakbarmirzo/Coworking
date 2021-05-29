from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update, Message
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,MessageHandler,Filters,CallbackContext,ConversationHandler

from const import TOKEN

phoneNumber="Ko'rsatilmagan❗️"
name="Ko'rsatilmagan❗️"
surname="Ko'rsatilmagan❗️"
group="Ko'rsatilmagan❗️"
teacher="Ko'rsatilmagan❗️"
apply='Berilmagan❌'

BTN_PREV='⬅️Orqaga'

STATE_RGISTRATION=1
STATE_BAND=1
STATE_USERINFO=1
STATE_ENTRYINFO=1

def start(update, context):
    user= update.message.from_user

    buttons = [
        [
            InlineKeyboardButton('Telefon ✏️',callback_data='phone_number'),
            InlineKeyboardButton('Ism ✏️', callback_data='name')
            ],
        [
            InlineKeyboardButton('Familiya ✏️', callback_data='surname'),
            InlineKeyboardButton('Guruh ✏️', callback_data='group')
        ],
        [
            InlineKeyboardButton("O'qtuvchi ✏️", callback_data='teacher')
        ]
    ]


    update.message.reply_html('''Assalomu alaykum <b>{}</b>\n<i>Coworkingga xush kelibsiz</i> \n
    Mening ma'lumotlarim \n 
    Telefon: {} 
    Ism: {} 
    Familiya: {} 
    Guruh: {} 
    O'qtuvchi: {} 
    Ruxsat: {}'''.format(user.first_name,phoneNumber,name,surname,group,teacher,apply), reply_markup=InlineKeyboardMarkup(buttons))

    return STATE_ENTRYINFO


def innline_callback(update: Update, _: CallbackContext):
    print(Update)

    query=update.callback_query

    prev=[
        [InlineKeyboardButton("⬅️Orqaga", callback_data='prev')]
    ]


    buttons = [
        [
            InlineKeyboardButton('Telefon ✏️',callback_data='phone_number'),
            InlineKeyboardButton('Ism ✏️', callback_data='name')
            ],
        [
            InlineKeyboardButton('Familiya ✏️', callback_data='surname'),
            InlineKeyboardButton('Guruh ✏️', callback_data='group')
        ],
        [
            InlineKeyboardButton("O'qtuvchi ✏️", callback_data='teacher')
        ]
    ]


    if query.data=='phone_number':
        query.edit_message_text(text="Telefoningizni kiriting. \nMasalan: +998930065969", reply_markup=InlineKeyboardMarkup(prev))
        # global phoneNumber
        
        
    if query.data=='prev':
        query.edit_message_text('''Mening ma'lumotlarim \n 
    Telefon: {} 
    Ism: {} 
    Familiya: {} 
    Guruh: {} 
    O'qtuvchi: {} 
    Ruxsat: {}'''.format(phoneNumber,name,surname,group,teacher,apply), reply_markup=InlineKeyboardMarkup(buttons))





def f_phone_number(update,context):
    update.message.reply_text("Phone number")
        





def main():
    updater=Updater(TOKEN, use_context=True)
    dispacher= updater.dispatcher

    # Start bosilganda
    dispacher.add_handler(CommandHandler('start', start))


    # inline buttonlar bosilganda
    conv_handler=ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_ENTRYINFO:[
                CallbackQueryHandler(innline_callback),
                MessageHandler(Filters.text & ~Filters.command, innline_callback)
                ],
            STATE_USERINFO: [
                # MessageHandler(Filters.regex('^(⬅️Orqaga)$')),
                # MessageHandler(Filters.regex('^(Telefon ✏️)$'))
            ],

        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispacher.add_handler(CallbackQueryHandler(innline_callback))
    # dispacher.add_handler(CallbackQueryHandler(info))

    # dispacher.add_handler(MessageHandler(Filters.text & ~Filters.command, info))

    updater.start_polling()
    updater.idle()


main()
if __name__ == '__main__':
    print("Worked")  