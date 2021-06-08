from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update, Message
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,MessageHandler,Filters,CallbackContext,ConversationHandler
from telegram.replymarkup import ReplyMarkup
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup

from const import TOKEN

phoneNumber="Ko'rsatilmagan❗️"
name="Ko'rsatilmagan❗️"
surname="Ko'rsatilmagan❗️"
group="Ko'rsatilmagan❗️"
teacher="Ko'rsatilmagan❗️"
apply='Berilmagan❌'


chack_info=False

BTN_APPLY="Ruxsat so'rash ✉️"
btn_apply=ReplyKeyboardMarkup([
    [BTN_APPLY]
],resize_keyboard=True)


KnowData=''
BTN_TEACHER="O'qtuvchi ✏️"
BTN_PREV='⬅️Orqaga'

STATE_TEACHER=1
STATE_USERINFO=1
STATE_ENTRYINFO=1

def start(update, context):
    user= update.message.from_user
    print(user)

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
            InlineKeyboardButton(BTN_TEACHER, callback_data='teacher')
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





def takePhone(update: Update, _: CallbackContext) -> None:
    """Echo the user message."""
    # print(update.message.text)
    global phoneNumber
    global name
    global surname
    global group
    global teacher
    if KnowData=='phone_number':
        phoneNumber=update.message.text
    elif KnowData=='name':
        name=update.message.text
    elif KnowData=='surname':
        surname=update.message.text
    elif KnowData=='group':
        group=update.message.text
    elif KnowData=='teacher':
        teacher=update.message.text

    else:
        print(update.message.text)
   

def innline_callback(update: Update, _: CallbackContext)-> None:
    

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
        global KnowData
        KnowData='phone_number'
        query.edit_message_text(text="Telefoningizni kiriting. \nMasalan: +998930065969", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO
        # global phoneNumber
        
        
    if query.data=='prev':
        query.message.reply_text('''Mening ma'lumotlarim \n 
            Telefon: {} 
            Ism: {} 
            Familiya: {} 
            Guruh: {} 
            O'qtuvchi: {} 
            Ruxsat: {}'''.format(phoneNumber,name,surname,group,teacher,apply), reply_markup=InlineKeyboardMarkup(buttons))

    if query.data=='name':
        KnowData='name'
        query.message.reply_text(text="Ismingizni kiriting kiriting.", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO
        
    if query.data=='surname':
        KnowData='surname'
        query.message.reply_text(text="Familiyangizni kiriting kiriting.", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO

    if query.data=='group':
        KnowData='group'
        query.message.reply_text(text="Guruhingizni kiriting kiriting.", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO

    if query.data=='teacher':
        KnowData='teacher'
        query.message.reply_text(text="O'qtuvchingizni kiriting kiriting.", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO

    if (phoneNumber !='' and phoneNumber !="Ko'rsatilmagan❗️" and name !='' and name !="Ko'rsatilmagan❗️" and surname!='' and surname != "Ko'rsatilmagan❗️" and group !='' and group != "Ko'rsatilmagan❗️" and teacher!= '' and teacher!= "Ko'rsatilmagan❗️"):
        query.message.reply_text(text="So'rov jo'natish 👇", reply_markup=btn_apply)
        
   






def f_phone_number(update,context):
    update.message.reply_text("Phone number")
        





def main():
    updater=Updater(TOKEN, use_context=True)
    dispacher= updater.dispatcher

    # Start bosilganda
    # dispacher.add_handler(CommandHandler('start', start))


    # inline buttonlar bosilganda
    conv_handler=ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_ENTRYINFO:[
                CallbackQueryHandler(innline_callback),
                # MessageHandler(Filters.text & ~Filters.command, e)
                ],
            STATE_USERINFO: [
                MessageHandler(Filters.text & ~Filters.command, takePhone),
                
            ],
            STATE_TEACHER: [

            ]


        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispacher.add_handler(CallbackQueryHandler(innline_callback))
    dispacher.add_handler(CallbackQueryHandler(takePhone))


    dispacher.add_handler(MessageHandler(Filters.text & ~Filters.command, takePhone))

   
    # dispacher.add_handler(CallbackQueryHandler(info))

    # dispacher.add_handler(MessageHandler(Filters.text & ~Filters.command, info))
    dispacher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


main()
if __name__ == '__main__':
    print("Worked")  