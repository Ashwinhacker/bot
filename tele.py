import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = [""] #use you Token 

ALLOWED_COMMANDS = ['ls', 'pwd', 'whoami', 'uptime', 'df', 'free', 'apt', 'install', 'get', 'git clone' , 'ping' ,'cls', 'dir', 'cat','clear' ]

async def reply(update: Update, context) -> None:
    user_message = update.message.text.strip().split()  
    command = user_message[0]  

    if command in ALLOWED_COMMANDS:
        try:
            result = subprocess.check_output(user_message, shell=False, text=True)
            print(result)
            await update.message.reply_text(f"Shell output:\n{result}")
        except subprocess.CalledProcessError as e:
            print(f"Command error: {e}")
            await update.message.reply_text(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            await update.message.reply_text(f"An unexpected error occurred: {e}")
    else:
        await update.message.reply_text(f"Command '{command}' is not allowed.")

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, reply))
    app.run_polling()

if __name__ == "__main__":
    main()
