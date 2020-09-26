from telegram.ext import CommandHandler

def help():
    return """
    猜一个0-100之间的数字。You guessed a number from 0 - 100.
/guess 查看现在的状态和获取帮助。Check your current status and get help.
/guess number 输入number猜数字，看谁用的次数最少。Enter number and see who uses it the least often.
    """

def response_guess(update, context):
    print(context.args)
    if len(context.args) == 0 :
        update.message.reply_text(help())
    else:
        number = int(context.args[0])
        update.message.reply_text("you said %s"%number)


def add_dispatcher(dispatcher):
    response_guess_handler = CommandHandler('guess', response_guess)#文字
    dispatcher.add_handler(response_guess_handler)