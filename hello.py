from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import os

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="命运指引我与你相见了，你有什么想要和我说的吗？")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('TOKEN')
print(TOKEN)

updater = Updater(token='TOKEN', use_context=True)#建立连接
dispatcher = updater.dispatcher#接收消息

start_handler = CommandHandler('start', start)#start函数加到dispatch
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)#文字
dispatcher.add_handler(echo_handler)

updater.start_polling()#开始接受所有数据