import Constants as constants
from telegram.ext import *


def start_command(update, context):
    update.message.reply_text("Bot started.")


def add_command(update, context):
    return


def set_command(update, context):
    return


def reset_command(update, context):
    return


def display_command(update, context):
    return


def error(update, context):
    print(f"Update {update} caused error {context.error}!")


def main():
    update = Updater(constants.API_KEY)

    print("Bot started")

    dp = update.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("add", add_command))
    dp.add_handler(CommandHandler("display", display_command))
    dp.add_handler(CommandHandler("set", set_command))
    dp.add_handler(CommandHandler("reset", reset_command))
    dp.add_error_handler(error)

    update.start_polling()
    update.idle()


main()
