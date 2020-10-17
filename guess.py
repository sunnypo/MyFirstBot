import random
from telegram.ext import CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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

    bigButton = InlineKeyboardButton('大',callback_data='big')
    smallButton = InlineKeyboardButton('小',callback_data='small')
    okButton = InlineKeyboardButton('确认',callback_data='ok')
    nullButton = InlineKeyboardButton('kon-kon',callback_data='bored')

    keyBoard = InlineKeyboardMarkup([[bigButton],[smallButton],[okButton],[nullButton]])

    if len(context.args) == 0 :
        update.message.reply_text(help(),reply_markup=keyBoard)
    else:
        if context.args[0].isdigit():
            number = int(context.args[0])
            userName = update.message.from_user.first_name
            if userName in games[chatid]:
                games[chatid]['member'] += 1
            else:
                games[chatid]['member'] = 1
            update.message.reply_text("you said %s, %s"%(number, userName),reply_markup=keyBoard)
            if number == games[chatid]['answerNumber']:
                update.message.reply_text("%s is the right number"%number,reply_markup=keyBoard)
                answerNumber = random.randint(0, 1000)
            elif number < games[chatid]['answerNumber']:
                update.message.reply_text("%sfrom %s is too small"%(number,userName),reply_markup=keyBoard)
            elif number > games[chatid]['answerNumber']:
                update.message.reply_text("%sfrom %s is too big"%(number,userName),reply_markup=keyBoard)
        else :
            update.message.reply_text("your answer %s is not number"%context.args[0],reply_markup=keyBoard)

def buttonCallBack(update, context):
    query = update.callback_query
    query.answer("啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊%s clicked %s"%(update.effective_user.first_name,query.data),show_alert=True)




def add_dispatcher(dispatcher):
    response_guess_handler = CommandHandler('guess1000', response_guess)#文字
    dispatcher.add_handler(response_guess_handler)
    dispatcher.add_handler(CallbackQueryHandler(buttonCallBack))