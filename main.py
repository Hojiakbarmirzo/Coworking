from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update, Message
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler,MessageHandler,Filters,CallbackContext,ConversationHandler
from telegram.replymarkup import ReplyMarkup
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup

from const import TOKEN
from const import ADMIN

phoneNumber="Ko'rsatilmagan❗️"
name="Ko'rsatilmagan❗️"
surname="Ko'rsatilmagan❗️"
group="Ko'rsatilmagan❗️"
teacher="Ko'rsatilmagan❗️"
apply='Berilmagan❌'


chack_info=False


btn_apply = [ 
    [ InlineKeyboardButton("Ruxsat so'rash ✉️", callback_data='request')]
]

control_apply_btn=[
        [
            InlineKeyboardButton('Ruxsat berish ✅', callback_data='True'),
            InlineKeyboardButton('Rad etish ❌', callback_data='False')
        ]
    ]  

KnowData=''

User_id=0

STATE_TEACHER=1
STATE_USERINFO=1
STATE_ENTRYINFO=1

def start(update, context):
    user= update.message.from_user

    global User_id
    User_id=user.id
    # print(user.id)

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





def takePhone(update, context) -> None:

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
   

def innline_callback(update, context):
    

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
    if query.data=="True":
        context.bot.send_message('1023834871', text='Ruxsat berildi')
        query.message.reply_text(text='Ruxsat berildi')

    if query.data=="False":
        
        query.message.reply_text(text='Ruxsat berilmadidi')



    if query.data=='request':
        query.edit_message_text(text="Ma'lumotlaringiz adminga yuborildi. Yaqin orada javobini olasiz")
        context.bot.send_message(ADMIN, text='''O'quvchining ma'lumotlari \n 
             Telefon: {} 
             Ism: {} 
             Familiya: {} 
             Guruh: {} 
             O'qtuvchi: {} 
             Ruxsat: {}'''.format(phoneNumber,name,surname,group,teacher,apply), reply_markup=InlineKeyboardMarkup(control_apply_btn))


    if query.data=='phone_number':
        print(update.callback_query.message.chat.id)
        global KnowData
        KnowData='phone_number'
        context.bot.send_message(update.callback_query.message.chat.id ,text="Telefoningizni kiriting. \nMasalan: +998930065969", reply_markup=InlineKeyboardMarkup(prev))
        # query.edit_message_text(text="Telefoningizni kiriting. \nMasalan: +998930065969", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO
        # global phoneNumber
        
        
    if query.data=='prev':
        context.bot.send_message(update.callback_query.message.chat.id , text='''Mening ma'lumotlarim \n 
            Telefon: {} 
            Ism: {} 
            Familiya: {} 
            Guruh: {} 
            O'qtuvchi: {} 
            Ruxsat: {}'''.format(phoneNumber,name,surname,group,teacher,apply), reply_markup=InlineKeyboardMarkup(buttons))

    if query.data=='name':
        KnowData='name'
        context.bot.send_message(update.callback_query.message.chat.id , text="Ismingizni kiriting kiriting.", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO
        
    if query.data=='surname':
        KnowData='surname'
        context.bot.send_message(update.callback_query.message.chat.id ,text="Familiyangizni kiriting kiriting.", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO

    if query.data=='group':
        KnowData='group'
        context.bot.send_message(update.callback_query.message.chat.id ,text="Guruhingizni kiriting kiriting.", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO

    if query.data=='teacher':
        KnowData='teacher'
        context.bot.send_message(update.callback_query.message.chat.id ,text="O'qtuvchingizni kiriting kiriting.", reply_markup=InlineKeyboardMarkup(prev))
        return STATE_USERINFO

    if (phoneNumber !='' and phoneNumber !="Ko'rsatilmagan❗️" and name !='' and name !="Ko'rsatilmagan❗️" and surname!='' and surname != "Ko'rsatilmagan❗️" and group !='' and group != "Ko'rsatilmagan❗️" and teacher!= '' and teacher!= "Ko'rsatilmagan❗️"):
        if update.callback_query.message.chat.id !=ADMIN:
            context.bot.send_message(update.callback_query.message.chat.id ,text="So'rov jo'natish 👇", reply_markup=InlineKeyboardMarkup(btn_apply))
        

        
   






def f_phone_number(update,context):
    update.message.reply_text("Phone number")
        





def main():
    updater=Updater(TOKEN, use_context=True)
    dispacher= updater.dispatcher

    # Start bosilganda
    dispacher.add_handler(CommandHandler('start', start))

   
    dispacher.add_handler(CallbackQueryHandler(innline_callback))
    dispacher.add_handler(CallbackQueryHandler(takePhone))


    dispacher.add_handler(MessageHandler(Filters.text & ~Filters.command, takePhone))




    updater.start_polling()
    updater.idle()


main()
if __name__ == '__main__':
    print("Worked")  