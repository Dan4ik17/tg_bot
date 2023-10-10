from telegram import ( 
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)


from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)


from cred import TOKEN
from menu import (
    main_menu_keyboard,
    courses_menu_keyboard,
)

from key_buttons import tele_button, courses


ABOUT =  tele_button[0]
COURSES = tele_button[1]
PYTHON = courses[0]
JAVA = courses[1]
JS = courses[2]
QA = courses[3]
BACK= courses[4]
LOCATION = tele_button[2]

def start(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Добро пожаловать {update.effective_user.username}\nэтот бот поможет вам с информацией о курсах',
        reply_markup = main_menu_keyboard()
    )
    
def about(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Преимущества обучения в Codify · Обучение с нуля до Junior.\nПройди обучение по авторской программе Codify и стань Junior специалистом.\nБольше о нас на https://www.codifylab.com'
    )
    
def reply_courses(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Choose corse',
        reply_markup = courses_menu_keyboard()
    )


def python(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Курс по Python вы можете изучить на сайте\nhttps://www.codifylab.com/ru/course/12'
    )

def java(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Курс по Java вы можете изучить на сайте\nhttps://www.codifylab.com/ru/course/16'
    )

def js(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Курс по JS вы можете изучить на сайте\nhttps://www.codifylab.com/ru/course/10'
    )

def qa(update:Update, context:CallbackContext):
    update.message.reply_text(
        f'Курс по QA вы можете изучить на сайте\nhttps://www.codifylab.com/ru/course/10'
    )


def location(update:Update, context:CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of Codify'
    )
    update.message.reply_location(
        #42.82909025000069, 74.61687279022618
        longitude = 42.82909025000069,
        latitude= 74.61687279022618,
        reply_to_message_id=msg.message_id
    )


updater = Updater(token=TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ABOUT),
    about
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSES),
    reply_courses
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON),
    python
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JAVA),
    java
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS),
    js
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(QA),
    qa
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    start
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATION),
    location
))

updater.start_polling()
updater.idle()