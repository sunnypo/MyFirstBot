#!/usr/bin/env python3

from telegram import Update
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
from telegram import BotCommand,PhotoSize

def get_info_general(update : Update, context : CallbackContext):
    msg=str(update.message.reply_to_message[5])
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

    # msg += "%s"%(update.message.reply_to_message.photo[2])
    # context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

    # picture = send_photo(update.message.reply_to_message.photo[0].file_id,update.message.reply_to_message.photo[0].file_unique_id,update.message.reply_to_message.photo[0].width,update.message.reply_to_message.photo[0].height,update.message.reply_to_message.photo[0].file_size)
    # update.message.reply_picture(picture=picture ,caption=f"{update.message.from_user.first_name}")

def add_handler(dp: Dispatcher):    
    dp.add_handler(CommandHandler(["info_general"], get_info_general))
    return []
