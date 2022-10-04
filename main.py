from cgitb import text
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import os
from database import User

TOKEN = os.environ['TOKEN']


def start(update: Update, context: CallbackContext):
    """Starts with two buttons uz and ru
    """
    userid = update.message.from_user.id
    user = User(username=str(userid))
    keyboard = [[KeyboardButton(text='uz'), KeyboardButton(text='ru')]]
    update.message.reply_text(text='Welcome message.', reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))
    

def uz(update, context):
    """Have to create these buttons
    playlist yaratish, Barcha musiqalar, Playlistlar
    """
    pass

def creating_playlist(update, context):
    """This creates a table in the database 
    user-given name of
    """
    pass

def all_music(update, context):
    """Sends all music in specific table
    """
    pass

def playlists(update, context):
    """This craetes buttons with all playlist name
    """
    pass

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


updater.start_polling()
updater.idle()