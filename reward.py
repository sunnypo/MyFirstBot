
from telegram.ext import Dispatcher,CommandHandler
from telegram import BotCommand


def response_reward(update, context):
    update.message.reply_text("来啦来啦")

def add_dispatcher(dispatcher):
    response_reward_handler = CommandHandler('reward', response_reward)#文字
    dispatcher.add_handler(response_reward_handler)

def get_command():
    return [BotCommand('rewards','其实这里什么都没写')]