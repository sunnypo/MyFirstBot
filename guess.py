import random
from telegram.ext import CommandHandler


games = {}


def help():
    return """
    猜一个0-1000之间的数字。You guessed a number from 0 - 1000.
/guess 查看现在的状态和获取帮助。Check your current status and get help.
/guess number 输入number猜数字，看谁用的次数最少。Enter number and see who uses it the least often.
    """

def response_guess(update, context):
    global answerNumber
    chatid = update.message.chat.id
    print(context.args)
    if not (chatid in games):
        games[chatid] = {'answerNumber' : random.randint(0, 1000), 'member':{}}
    print(games)  
    if len(context.args) == 0 :
        update.message.reply_text(help())
    else:
        if context.args[0].isdigit():
            number = int(context.args[0])
            userName = update.message.from_user.first_name
            if userName in games[chatid]:
                games[chatid]['member'] += 1
            else:
                games[chatid]['member'] = 1
            update.message.reply_text("you said %s, %s"%(number, userName))
            if number == games[chatid]['answerNumber']:
                update.message.reply_text("%s is the right number"%number)
                answerNumber = random.randint(0, 1000)
            elif number < games[chatid]['answerNumber']:
                update.message.reply_text("%sfrom %s is too small"%(number,userName))
            elif number > games[chatid]['answerNumber']:
                update.message.reply_text("%sfrom %s is too big"%(number,userName))
        else :
            update.message.reply_text("your answer %s is not number"%context.args[0])


def add_dispatcher(dispatcher):
    response_guess_handler = CommandHandler('guess1000', response_guess)#文字
    dispatcher.add_handler(response_guess_handler)