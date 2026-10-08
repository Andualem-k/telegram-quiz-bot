import os
import threading
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

# Render እንዳይተኛ HTTP Web Server ማዘጋጀት
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!", 200

def run_flask():
    # Render የሚሰጠውን PORT ወይም በደባብ 8080 መጠቀም
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# --- የቦትህ ዋና ስራ ---
def main():
    # Flask Web Serverን ከጀርባ ማስነሳት
    threading.Thread(target=run_flask, daemon=True).start()

    # Bot Token ከ Render Environment ወይም ከጽሁፉ መውሰድ
    TOKEN = os.environ.get("BOT_TOKEN")
    
    if not TOKEN:
        # BOT_TOKEN በ Environment ካልተዋቀረ የራስህን Token እዚህ አድርገው
        TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE" 

    application = ApplicationBuilder().token(TOKEN).build()
    
    # -------------------------------------------------------------
    # ማስታወሻ፦ የነበሩህን Handlers (Quiz, Commands) ከዚህ በታች አክላቸው
    # -------------------------------------------------------------
    
    print("ቦቱ ሥራ ጀምሯል...")
    application.run_polling()

if __name__ == '__main__':
    main()
 
