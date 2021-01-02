from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import InlineKeyboardMarkup,InlineKeyboardButton,BotCommand
import random
from datetime import datetime,timedelta
import coins

bigButton = InlineKeyboardButton('大',callback_data='big')
smallButton = InlineKeyboardButton('小',callback_data='small')
checkOutButton = InlineKeyboardButton('结算',callback_data='checkOut')
dailyButton = InlineKeyboardButton('打卡',callback_data='daily')

keyBoard = InlineKeyboardMarkup([[bigButton,smallButton]])

joinButton = InlineKeyboardButton('加入',callback_data='join')
startButton = InlineKeyboardButton('开始',callback_data='start')

startkb = InlineKeyboardMarkup([[joinButton,startButton]])

timer = 0

# { first_name:d, :x}
games = {}

def check_chatid(chatid):
    if not chatid in games.keys():
        games[chatid]={
            "h":"",
            "p":{}
        }

def getHist(chatid):
    return games[chatid]['h']

def setHist(chatid,res):
    h = games[chatid]['h']
    if len(h) > 10:
        h = h[:9] + res
    else:
        h += res
    games[chatid]['h'] = h

def getNumber():
    endNumber = 0
    msg = ""
    for _i in range(3):
        rnumber = random.randint(1,6)
        endNumber += rnumber
        msg += "=%s"%rnumber
    msg += "=%s" % endNumber
    return [endNumber,msg]

def checkOutGame(chatid):
    number,msg = getNumber()
    users = games[chatid]["p"]
    game = '小'
    if number >= 11:
        game = '大'
    setHist(chatid,game)
    for u in users.keys():
        if users[u] == '':
            users[u] = '磨唧'
        elif users[u] == game:
            c = random.randint(0,10)
            coins.add_coins(chatid,u,c)
            users[u] = f'Yes! 你赢取了{c}个金币'
            coins.add_count(chatid,u)
        else:
            c = random.randint(0,10) * -1
            coins.add_coins(chatid,u,c)
            users[u] = f'Noo!你输掉了{c}个金币'
            coins.add_count(chatid,u)
    msg += "\n%s"%getUser(users)
    return msg 

def getUser(users):
    msg = ""
    for u in users.keys():
        print(u)
        msg += "%s:%s\n"%(u,games[u])
    return msg

def response_guess(update, context):
    global timer
    chatid = update.effective_chat.id
    check_chatid(chatid)
    timer = datetime.now() + timedelta(seconds=5)
    update.message.reply_text("请选择大或小",reply_markup=startkb)

def buttonCallBack(update, context):
    global games,timer
    query = update.callback_query
    chatid = update.effective_chat.id
    user = update.effective_user
    check_chatid(chatid)
    users = games[chatid]["p"]
    print(f"s:{games}")
    msg = getUser(users) + "\n\n" + getHist(chatid)
    if query.data == 'join':
        query.answer("加入游戏")
        users[update.effective_user] = ""
        query.edit_message_text(msg,reply_markup=startkb)
        return
    elif query.data == "daily":
        c = coins.daily(chatid,user)
        if c == 0:
            query.answer("别着急，每五分钟只能打一次卡",show_alert=True)
        else:
            query.answer(f"打卡成功，你得到了{c}个金币",show_alert=True)
    elif query.data == 'start':
        timenow = datetime.now()
        if timenow > timer:
            query.answer("开始")
            query.edit_message_text(msg,reply_markup=keyBoard)
            timer = datetime.now()+timedelta(seconds=5)
        else:
            query.answer("冷静！还没到五秒！",show_alert=True)
    elif query.data == 'big':
        if users == {}:
            return
        query.answer("你选择了大")
        users[update.effective_user] = "d"
        query.edit_message_text(msg,reply_markup=keyBoard)
    elif query.data == 'small':
        if users == {}:
            return
        query.answer("你选择了小")
        users[update.effective_user] = "x"
        query.edit_message_text(msg,reply_markup=keyBoard)
    elif query.data == 'sum':
        timenow = datetime.now()
        if timenow > timer:
            query.answer("结算开始")
            msg = checkOutGame(chatid)+ "\n\n" +getHist(chatid)
            query.edit_message_text(msg)
            users = {}
        else:
            query.answer("冷静！还没到五秒！",show_alert=True)
    games[chatid]["p"] = users
    print(f"e:{games}")

def add_dispatcher(dispatcher):
    response_guess_handler = CommandHandler('guess1000', response_guess)#文字
    dispatcher.add_handler(response_guess_handler)
    dispatcher.add_handler(CallbackQueryHandler(buttonCallBack))

def get_command():
    return [BotCommand('guess1000','选择困难？')]