#!/usr/bin/env python3

from telegram import Update
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
from telegram import BotCommand,PhotoSize

def get_info_picture(update : Update, context : CallbackContext):
    msg = ""
    for i in update.message.reply_to_message.photo:
        msg += "%s\n"%str(i)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def add_handler(dp: Dispatcher):
    dp.add_handler(CommandHandler(["info_picture"], get_info_picture))
    return []
