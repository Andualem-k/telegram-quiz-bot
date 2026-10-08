import logging
import os
import threading
from flask import Flask
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Questions file
from cs_questions import CS_EXIT_EXAM_2018

# 1. Render እንዳይተኛ HTTP Web Server (Port 8080)
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Quiz Bot is alive and running!", 200

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app_flask.run(host="0.0.0.0", port=port)

# 2. Logging & Configurations
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

FREE_QUESTIONS_LIMIT = 5
ADMIN_ID = 1519242710
ADMIN_USERNAME = '@anmg2828kt'

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton('🚀 Start'), KeyboardButton('🎯 Quiz Start')],
        [KeyboardButton('💳 Kfya / Payment'), KeyboardButton('ℹ️ Help / Admin')],
    ],
    resize_keyboard=True,
)

# 3. Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f'ሰላም {user_name}! 👋\n\n'
        f'እንኳን ወደ **የኮምፒውተር ሳይንስ Exit Exam ልምምድ ቦት** በደህና መጡ።\n\n'
        f'📌 የመጀመሪያዎቹን {FREE_QUESTIONS_LIMIT} ጥያቄዎች በነጻ መሞከር ይችላሉ!\n'
        f'ከታች ያሉትን አዝራሮች (Buttons) በመጠቀም መጀመር ይችላሉ።'
    )
    await update.message.reply_text(
        welcome_text, reply_markup=MAIN_KEYBOARD, parse_mode='Markdown'
    )

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['current_index'] = 0
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        index = context.user_data.get('current_index', 0)
        chat_id = update.effective_chat.id

        # 1. Check Free Limit
        if index >= FREE_QUESTIONS_LIMIT and not context.user_data.get('is_paid', False):
            payment_text = (
                f'🔒 **የነጻ ልምምድ ገደብ አልቋል!**\n\n'
                f'የነጻ ፈተና እድልዎ ({FREE_QUESTIONS_LIMIT} ጥያቄዎች) ተጠናቋል። ሁሉንም 100 ጥያቄዎች ለማግኘት የ **100 ብር** ክፍያ ይፈጽሙ።\n\n'
                f'💳 **የክፍያ አማራጮች፦**\n'
                f'• **Telebirr / CBE፦** `0934234392`\n'
                f'• **የአካውንት ስም፦** Kebede Assefa\n\n'
                f'📩 **የክፍያ ማረጋገጫ ለመላክ፦**\n'
                f'የከፈሉበትን ደረሰኝ (Screenshot) ለ Admin ይላኩ፦ {ADMIN_USERNAME}\n\n'
                f'ክፍያዎ እንደተረጋገጠ ቦቱ ይከፈትልዎታል።'
            )
            await context.bot.send_message(chat_id=chat_id, text=payment_text, parse_mode='Markdown')
            return

        # 2. Check Exam End
        if index >= len(CS_EXIT_EXAM_2018):
            text = '🎉 **እንኳን ደስ አለዎት! ሁሉንም ጥያቄዎች ጨርሰዋል።**'
            await context.bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown')
            return

        # 3. Send Question
        q = CS_EXIT_EXAM_2018[index]
        letters = ['A', 'B', 'C', 'D', 'E', 'F']

        keyboard = []
        for opt_idx, option in enumerate(q['options']):
            letter_prefix = letters[opt_idx] if opt_idx < len(letters) else f'{opt_idx+1}'
            button_label = f'{letter_prefix}. {option}'
            keyboard.append([InlineKeyboardButton(button_label, callback_data=f'ans|{opt_idx}')])

        reply_markup = InlineKeyboardMarkup(keyboard)
        question_text = f"**ጥያቄ {q['id']} / {len(CS_EXIT_EXAM_2018)}**\n\n{q['question']}"

        await context.bot.send_message(
            chat_id=chat_id,
            text=question_text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    except Exception as e:
        print(f'Error occurred in send_question: {e}')

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    opt_idx = int(query.data.split('|')[1])
    index = context.user_data.get('current_index', 0)

    if index >= len(CS_EXIT_EXAM_2018):
        index = 0
        context.user_data['current_index'] = 0

    q = CS_EXIT_EXAM_2018[index]
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    letter_prefix = letters[opt_idx] if opt_idx < len(letters) else f'{opt_idx+1}'

    user_choice = q['options'][opt_idx]
    user_choice_formatted = f'{letter_prefix}. {user_choice}'

    if str(user_choice).strip() == str(q['correct_answer']).strip():
        result_text = (
            f'✅ **ትክክል ነው!**\n\n'
            f"🎯 **መልስ፦** {q['correct_answer']}\n"
            f"💡 **ማብራሪያ፦** {q['explanation']}"
        )
    else:
        result_text = (
            f'❌ **ተሳስቷል!**\n\n'
            f'የመረጡት፦ {user_choice_formatted}\n'
            f"🎯 **ትክክለኛው መልስ፦** {q['correct_answer']}\n\n"
            f"💡 **ማብራሪያ፦** {q['explanation']}"
        )

    next_keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton('ቀጣይ ጥያቄ ➡️', callback_data='next_q')]]
    )

    await query.edit_message_text(text=result_text, reply_markup=next_keyboard, parse_mode='Markdown')

async def next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    current_index = context.user_data.get('current_index', 0)
    context.user_data['current_index'] = current_index + 1
    await send_question(update, context)

async def handle_text_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == '🚀 Start':
        await start(update, context)
    elif text == '🎯 Quiz Start':
        await start_quiz(update, context)
    elif text == '💳 Kfya / Payment':
        payment_info = (
            f'💳 **የክፍያ መረጃ**\n\n'
            f'• **Telebirr / CBE፦** `0934234392`\n'
            f'• **የአካውንት ስም፦** Kebede Assefa\n'
            f'• **ክፍያ፦** 100 Birr\n\n'
            f'ከከፈሉ በኋላ ደረሰኙን ለ Admin ይላኩ፦ {ADMIN_USERNAME}'
        )
        await update.message.reply_text(payment_info, parse_mode='Markdown')
    elif text == 'ℹ️ Help / Admin':
        await update.message.reply_text(f'ለማንኛውም ጥያቄ ወይም እርዳታ Adminን ያናግሩ፦ {ADMIN_USERNAME}')

async def approve_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('❌ ይቅርታ! ይህንን ማድረግ የሚችለው Admin ብቻ ነው።')
        return

    if not context.args:
        await update.message.reply_text('⚠️ ID ያስገቡ! (ምሳሌ፦ `/approve 987654321`)', parse_mode='Markdown')
        return

    try:
        user_id_to_approve = int(context.args[0])
        user_data = context.application.user_data.setdefault(user_id_to_approve, {})
        user_data['is_paid'] = True

        await update.message.reply_text(
            f'✅ ተጠቃሚ ID `{user_id_to_approve}` ተከፍቷል!',
            parse_mode='Markdown',
        )
        await context.bot.send_message(
            chat_id=user_id_to_approve,
            text='🎉 **ክፍያዎ ተረጋግጧል!**\n\nአሁን ሁሉንም ጥያቄዎች መስራት ይችላሉ።',
            parse_mode='Markdown',
        )
    except Exception as e:
        await update.message.reply_text(f'ስህተት ተፈጠረ፦ {e}')

# 4. Main Execution
if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8809032194:AAGpO0DPvCW87RMj-BulJempz8dEMwciJxE")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('quiz', start_quiz))
    app.add_handler(CommandHandler('approve', approve_user))
    app.add_handler(CallbackQueryHandler(handle_answer, pattern='^ans\|'))
    app.add_handler(CallbackQueryHandler(next_question, pattern='^next_q\$'))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_buttons))

    print('ቦቱ ሥራ ጀምሯል...')
    app.run_polling()
