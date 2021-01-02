from telegram.ext import Dispatcher,CommandHandler,CallbackQueryHandler
from telegram import BotCommand,InlineKeyboardMarkup,InlineKeyboardButton
import random

# messageid: [uid,uid,uid...]
uservote = {}

def vote(update,context):
    gifs = [
        ""
    ]
    #  [[👍,👎,😍]]
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("👍(0)",callback_data="vote:👍:0"),
        InlineKeyboardButton("👎(0)",callback_data="vote:👎:0"),
        InlineKeyboardButton("😍(0)",callback_data="vote:😍:0")
        ]])
    jif = random.choice(gifs)
    update.message.reply_animation(jif,caption="迷迭迷迭",reply_markup=kb)

def add_user_vote(mid,uid):
    if not mid in uservote :
        uservote[mid] = []
    if not uid in uservote[mid] :
        uservote[mid].append(uid)
        return True # 之没投过
    return False # 之前投过票了

def vote_callback(update,context):
    query = update.callback_query
    cmd = query.data.split(":") # ['vote','👍']
    buttons = query.message.reply_markup.inline_keyboard
    mid = query.message.message_id
    uid = update.effective_user.id

    if add_user_vote(mid,uid) :
        count = int(cmd[2]) + 1
        query.answer("投好了")
        if cmd[1] == '👍':
            buttons[0][0] = InlineKeyboardButton(f"👍({count})",callback_data=f"vote:👍:{count}")
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        elif cmd[1] == "👎":
            buttons[0][1] = InlineKeyboardButton(f"👎({count})",callback_data=f"vote:👎:{count}")
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
        elif cmd[1] == "😍":
            buttons[0][2] = InlineKeyboardButton(f"😍({count})",callback_data=f"vote:😍:{count}")
            query.edit_message_reply_markup(InlineKeyboardMarkup(buttons))
    else:
        query.answer("你只有一次机会",show_alert=True)


def add_handler(dp:Dispatcher):
    dp.add_handler(CommandHandler('vote', vote))
    dp.add_handler(CallbackQueryHandler(vote_callback,pattern="^vote:[A-Za-z0-9_:]*"))

def get_command():
    return [BotCommand('vote','你喜欢哪个？')]