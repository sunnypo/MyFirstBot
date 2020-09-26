import random
from telegram.ext import CommandHandler


def response_guess(update, context):
    randomList = ["再走一遍老路也并不算坏事，-100XP", "命运终会犒赏努力的人，好好睡一觉吧，+1000XP", "奖赏一如既往，你为自己感到自豪，+500XP"]
    number = random.randrange(0, 4)
    if number == 3 :
        randomXP = random.randrange(500, 1000)
        message_reply = "争论不休, 迟迟没有结果。他们取了个平均数，+%sXP"%(randomXP)
    else:
        message_reply = randomList[number]
    msg = "现在是%s的封赏之时, 请命运指引我们到更光辉到明天吧 \n\"%s\" "%(update.message.from_user.first_name, message_reply)
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)

def add_dispatcher(dispatcher):
    response_guess_handler = CommandHandler('guess', response_guess)#文字
    dispatcher.add_handler(response_guess_handler)