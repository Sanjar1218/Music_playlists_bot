from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
import os
from database import User

TOKEN = os.environ['TOKEN']


def start(update: Update, context: CallbackContext):
    """Starts with two buttons uz and ru
    """
    userid = update.message.from_user.id
    user = User(username=str(userid))
    keyboard = [[KeyboardButton(text='uz'), KeyboardButton(text='ru')]]
    update.message.reply_text(text='Welcome message.', reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))
    

def uz(update: Update, context: CallbackContext):
    """Have to create these buttons
    playlist yaratish, Barcha musiqalar, Playlistlar
    """
    keyboard = [
            [
                KeyboardButton(text='PLaylistlar'),
                KeyboardButton(text='Barcha Musiqalar'), 
                KeyboardButton(text='Playlist Yaratish'), 
            ],
            [KeyboardButton(text='Orqaga')]
        ]
    update.message.reply_text(text='uz', reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

def creating_playlist(update, context):
    """This creates a table in the database 
    user-given name of
    """
    pass

def all_music(update, context):
    """Sends all music in specific table
    """
    pass

def playlists(update: Update, context: CallbackContext):
    """This craetes buttons with all playlist name
    """
    msg = update.message
    user_id = msg.from_user.id
    user = User(username=str(user_id))
    pls = user.all_pl()
    if not pls:
        return msg.reply_text(text="Playlist mavjud emas!")
    inline_keyboard = []
    for pl in pls:
        inline_btn = InlineKeyboardButton(text=pl, callback_data=pl)
        inline_keyboard.append([inline_btn])
    return msg.reply_text(text="PLaylistlar", reply_markup=InlineKeyboardMarkup(inline_keyboard=inline_keyboard))

def music(update, context):
    """A music message with two inline buttons
    like button and delete button
    """
    pass

def get_music(update, context):
    """When user sends music its have to ask playlist name
    then adds to this playlist ids in database

    """
    pass


updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(handler=CommandHandler(command=['start', 'boshlash'], callback=start))
dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('uz'), callback=uz))
dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('Orqaga'), callback=start))
dispatcher.add_handler(handler=MessageHandler(filters=Filters.text('PLaylistlar'), callback=playlists))


updater.start_polling()
updater.idle()