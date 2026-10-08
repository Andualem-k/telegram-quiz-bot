import os
import logging
import threading
from flask import Flask
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# 1. Render እንዳይተኛ የሚያደርግ Flask Web Server
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive and running!", 200

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# 2. የቴሌግራም ቦት ተግባራት (Handlers)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ሰላም! ወደ Quiz Bot እንኳን ደህና መጡ። /quiz ብለው ይጀምሩ።")

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("የፈተና ጥያቄዎች እዚህ ይጀምራሉ...")

# 3. ዋናው ማስነሻ function
def main():
    # Flask Web Server ከጀርባ እንዲሰራ ማድረግ
    threading.Thread(target=run_flask, daemon=True).start()

    TOKEN = os.environ.get("BOT_TOKEN")
    if not TOKEN:
        # BOT_TOKEN በ Render ላይ ካልተዋቀረ የራስህን Token እዚህ ጋር አድርገው
        TOKEN = "YOUR_BOT_TOKEN_HERE"

    application = ApplicationBuilder().token(TOKEN).build()

    # Handlers መጨመር
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("quiz", quiz))

    # የነበሩህን ተጨማሪ Handlers እና Quiz Logic እዚህ ማከል ትችላለህ

    print("ቦቱ ሥራ ጀምሯል...")
    application.run_polling()

if __name__ == '__main__':
    main()
