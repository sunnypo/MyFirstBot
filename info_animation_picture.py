#!/usr/bin/env python3

from telegram import Update
from telegram.ext import Dispatcher,CommandHandler,CallbackContext
from telegram import BotCommand,Animation,PhotoSize

def get_info_animation(update : Update, context : CallbackContext):
    file_id = str("file_id = %s"%(update.message.reply_to_message.animation.file_id))
    file_unique_id = str("file_unique_id = %s"%(update.message.reply_to_message.animation.file_unique_id))
    width = str("width = %s"%(update.message.reply_to_message.animation.width))
    height = str("height = %s"%(update.message.reply_to_message.animation.height))
    duration = str("duration = %s"%(update.message.reply_to_message.animation.duration))
    file_name = str("file_name = %s"%(update.message.reply_to_message.animation.file_name))
    file_size = str("file_size = %s"%(update.message.reply_to_message.animation.file_size))

    msg = "%s\n%s\n%s\n%s\n%s\n%s\n%s\n"%(file_id, file_unique_id, width, height, duration, file_name, file_size)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

    animation = Animation(update.message.reply_to_message.animation.file_id,update.message.reply_to_message.animation.file_unique_id,update.message.reply_to_message.animation.width,update.message.reply_to_message.animation.height,update.message.reply_to_message.animation.file_size)
    update.message.reply_animation(animation = animation ,caption=f"{update.message.from_user.first_name}")

def get_info_picture(update : Update, context : CallbackContext):
    msg = ""
    
    msg += "%s\n"%(update.message.reply_to_message.photo[2])
        
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

    # picture = send_photo(update.message.reply_to_message.photo[0].file_id,update.message.reply_to_message.photo[0].file_unique_id,update.message.reply_to_message.photo[0].width,update.message.reply_to_message.photo[0].height,update.message.reply_to_message.photo[0].file_size)
    # update.message.reply_picture(picture=picture ,caption=f"{update.message.from_user.first_name}")

def add_handler(dp: Dispatcher):
    dp.add_handler(CommandHandler(["info_animation"], get_info_animation))
    dp.add_handler(CommandHandler(["info_picture"], get_info_picture))
    return []