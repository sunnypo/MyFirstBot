#!/usr/bin/env python3

from telegram import Update
from telegram.ext import Dispatcher,CommandHandler,CallbackContext

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


def add_handler(dp: Dispatcher):
    dp.add_handler(CommandHandler(["info_animation"], get_info_animation))
    return []
