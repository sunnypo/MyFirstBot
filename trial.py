import random
from telegram.ext import CommandHandler

def response(update, context):
    randomList = ["再走一遍老路也并不算坏事，-1000XP", "命运终会犒赏努力的人，好好睡一觉吧，+1000XP", "审判一如既往，你更加感受到了自己的弱小，-500XP"]
    number = random.randrange(0, 4)
    if number == 3 :
        randomXP = random.randrange(500, 1000)
        message_reply = "争论不休, 迟迟没有结果。你献祭了%sXP只为了不再听无尽的废话"%(randomXP)
    else:
        message_reply = randomList[number]
    msg = "现在是%s的审判之时, 请命运指示我们前进的道路吧 \n\"%s\" "%(update.message.from_user.first_name, message_reply)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def add_dispatcher(dispatcher): 
    response_handler = CommandHandler('trial', response)#文字
    dispatcher.add_handler(response_handler)



