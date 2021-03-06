from telegram.ext import Updater,MessageHandler, Filters,CommandHandler
from telegram import BotCommand
import os
import random
import trail
import reward
import guess
import coins
import vote
import info_animation_picture
import info_general

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="命运指引我们相见了……有什么想要和我说的吗？（审判请发送“/trial”）")

def echo(update, context):
    print(update)
    print(update.message.from_user.first_name)
    msg = "%s, \"%s\"吗? 无论如何，还是谢谢你和我说了这些。"%(update.message.from_user.first_name, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def read_file_as_str(file_path):
    # 判断路径文件存在
    if not os.path.isfile(file_path):
        raise TypeError(file_path + " does not exist")

    # 读取文件内容到all_the_text
    all_the_text = open(file_path).read()
    # print type(all_the_text)
    return all_the_text

TOKEN=read_file_as_str('TOKEN')

updater = Updater(token=TOKEN, use_context=True)#建立连接
dispatcher = updater.dispatcher#接收消息

trail.add_dispatcher(dispatcher)
reward.add_dispatcher(dispatcher)
guess.add_dispatcher(dispatcher)
coins.add_handler(dispatcher)
vote.add_handler(dispatcher)
info_animation_picture.add_handler(dispatcher)
info_general.add_handler(dispatcher)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)#文字
dispatcher.add_handler(echo_handler)

commands = reward.get_command() + guess.get_command() 
bot = updater.bot
bot.set_my_commands(commands)

start_handler = CommandHandler('start', start)#start函数加到dispatch
dispatcher.add_handler(start_handler)

updater.start_polling()#开始接受所有数据