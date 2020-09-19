# from telegram.ext import Updater
# from telegram.ext import CommandHandler
# from telegram.ext import MessageHandler, Filters

# def echo(update, context):
#     print(update)
#     print(update.message.from_user.first_name)
#     msg = "%s, \"%s\"吗? 无论如何，还是谢谢你和我说了这些。"%(update.message.from_user.first_name, update.message.text)
#     context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


# def response(update, context):
#     randomList = ["再走一遍老路也并不算坏事，-1000XP", "命运终会犒赏努力的人，好好睡一觉吧，+1000XP", "审判一如既往，你更加感受到了自己的弱小，-500XP"]
#     if update.message.text == "审判":
#         number = random.randrange(0, 101, 2)
#         if number == 3 :
#             randomXP = random.randrange(500, 1000)
#             message_reply = "争论不休, 迟迟没有结果。你献祭了%sXP只为了不再听无尽的废话"%(randomXP)
#         else:
#             message_reply = randomList[number]
#     msg = "现在是%s的审判之时, 请命运指示我们前进的道路吧 \n\"%s\" "%(update.message.from_user.first_name, message_reply)
#     context.bot.send_message(chat_id=update.effective_chat.id, text=msg)