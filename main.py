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

# Questions and Database modules
from cs_questions import CS_EXIT_EXAM_2018
from database import init_db, add_paid_user, is_user_paid, get_paid_users_count

# Initialize Database
init_db()

# 1. Render Keep-Alive HTTP Web Server
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

# Tech / Modern Style Keyboard
MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton('⚡ Main Menu'), KeyboardButton('💻 Start Exam Quiz')],
        [KeyboardButton('👑 Upgrade to PRO'), KeyboardButton('⚙️ Help & Support')],
        [KeyboardButton('🆔 My User ID')],
    ],
    resize_keyboard=True,
)

# 3. Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_text = (
        f"┌─── 🎓 **COMPUTER SCIENCE EXIT EXAM** ───┐\n"
        f"│ Welcome, **{user_name}**!\n"
        f"└──────────────────────────────────────┘\n\n"
        f"<code>Prep for your 2018 Exit Exam with interactive questions & detailed explanations.</code>\n\n"
        f"✨ **Trial Plan:** First {FREE_QUESTIONS_LIMIT} questions are **FREE**!\n"
        f"🔒 **PRO Plan:** Unlock all exam questions for just **100 ETB**.\n\n"
        f"👇 *Use the options below to begin:* "
    )
    await update.message.reply_text(
        welcome_text, reply_markup=MAIN_KEYBOARD, parse_mode='HTML'
    )

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['current_index'] = 0
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        index = context.user_data.get('current_index', 0)
        chat_id = update.effective_chat.id

        user_has_paid = is_user_paid(chat_id)

        if index >= FREE_QUESTIONS_LIMIT and not user_has_paid:
            payment_text = (
                f"🔒 <b>FREE TRIAL LIMIT REACHED</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n"
                f"You have completed your trial of <b>{FREE_QUESTIONS_LIMIT} free questions</b>.\n\n"
                f"💳 <b>Unlock Full PRO Access (100 ETB):</b>\n"
                f"• <b>Telebirr / CBE:</b> <code>0934234392</code>\n"
                f"• <b>Account Name:</b> Kebede Assefa\n\n"
                f"📩 <b>Activation Steps:</b>\n"
                f"Send receipt screenshot + your User ID (<code>{chat_id}</code>) to Admin: {ADMIN_USERNAME}\n\n"
                f"<i>Your account will be activated immediately!</i>"
            )
            await context.bot.send_message(chat_id=chat_id, text=payment_text, parse_mode='HTML')
            return

        if index >= len(CS_EXIT_EXAM_2018):
            text = "🎉 <b>CONGRATULATIONS!</b>\n\nYou have completed all available practice questions."
            await context.bot.send_message(chat_id=chat_id, text=text, parse_mode='HTML')
            return

        q = CS_EXIT_EXAM_2018[index]
        letters = ['A', 'B', 'C', 'D', 'E', 'F']

        keyboard = []
        for opt_idx, option in enumerate(q['options']):
            letter_prefix = letters[opt_idx] if opt_idx < len(letters) else f'{opt_idx+1}'
            button_label = f'{letter_prefix}. {option}'
            keyboard.append([InlineKeyboardButton(button_label, callback_data=f'ans|{index}|{opt_idx}')])

        reply_markup = InlineKeyboardMarkup(keyboard)
        question_text = (
            f"<b>QUESTION {q['id']} / {len(CS_EXIT_EXAM_2018)}</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{q['question']}"
        )

        await context.bot.send_message(
            chat_id=chat_id,
            text=question_text,
            reply_markup=reply_markup,
            parse_mode='HTML'
        )
    except Exception as e:
        logging.error(f'Error in send_question: {e}')

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    parts = query.data.split('|')
    q_index = int(parts[1])
    opt_idx = int(parts[2])

    if q_index >= len(CS_EXIT_EXAM_2018):
        return

    q = CS_EXIT_EXAM_2018[q_index]
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    letter_prefix = letters[opt_idx] if opt_idx < len(letters) else f'{opt_idx+1}'

    user_choice = q['options'][opt_idx]
    user_choice_formatted = f'{letter_prefix}. {user_choice}'

    if str(user_choice).strip() == str(q['correct_answer']).strip():
        result_text = (
            f"✅ <b>CORRECT ANSWER!</b>\n\n"
            f"🎯 <b>Answer:</b> {q['correct_answer']}\n\n"
            f"💡 <b>Explanation:</b>\n<code>{q['explanation']}</code>"
        )
    else:
        result_text = (
            f"❌ <b>INCORRECT ANSWER!</b>\n\n"
            f"<b>Your Choice:</b> {user_choice_formatted}\n"
            f"🎯 <b>Correct Answer:</b> {q['correct_answer']}\n\n"
            f"💡 <b>Explanation:</b>\n<code>{q['explanation']}</code>"
        )

    next_q_index = q_index + 1
    next_keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Next Question ➡️', callback_data=f'next|{next_q_index}')]]
    )

    await query.edit_message_text(text=result_text, reply_markup=next_keyboard, parse_mode='HTML')

async def next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    parts = query.data.split('|')
    next_q_index = int(parts[1])

    context.user_data['current_index'] = next_q_index
    await send_question(update, context)

async def handle_text_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if text in ['🚀 Start', '⚡ Main Menu']:
        await start(update, context)
    elif text in ['🎯 Start Quiz', '🎯 Quiz Start', '💻 Start Exam Quiz']:
        await start_quiz(update, context)
    elif text in ['💳 Payment / Upgrade', '👑 Upgrade to PRO']:
        status = "🟢 <b>PRO Active Member</b>" if is_user_paid(user_id) else "🔴 <b>Free Trial Plan</b>"
        payment_info = (
            f"👑 <b>CS EXIT EXAM - PRO MEMBERSHIP</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"• <b>Account Status:</b> {status}\n"
            f"• <b>Access Fee:</b> 100 ETB (Lifetime Access)\n"
            f"• <b>Telebirr / CBE:</b> <code>0934234392</code>\n"
            f"• <b>Account Holder:</b> Kebede Assefa\n\n"
            f"🆔 <b>Your Telegram ID:</b> <code>{user_id}</code>\n\n"
            f"<i>Send receipt screenshot to Admin:</i> {ADMIN_USERNAME}"
        )
        await update.message.reply_text(payment_info, parse_mode='HTML')
    elif text in ['ℹ️ Help / Admin', '⚙️ Help & Support']:
        await update.message.reply_text(f"🛠️ <b>Support Center</b>\n\nFor inquiries or manual approval, contact Admin: {ADMIN_USERNAME}", parse_mode='HTML')
    elif text == '🆔 My User ID':
        await update.message.reply_text(
            f"👤 <b>YOUR TELEGRAM USER ID</b>\n"
            f"<code>{user_id}</code>\n\n"
            f"<i>(Tap the number above to copy and send to Admin)</i>",
            parse_mode='HTML'
        )

async def approve_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('❌ Unauthorized! Admin only.')
        return

    if not context.args:
        await update.message.reply_text('⚠️ Provide User ID! Usage: <code>/approve USER_ID</code>', parse_mode='HTML')
        return

    try:
        user_id_to_approve = int(context.args[0])
        add_paid_user(user_id_to_approve)

        await update.message.reply_text(
            f'✅ User <code>{user_id_to_approve}</code> approved & stored in Database!',
            parse_mode='HTML',
        )
        await context.bot.send_message(
            chat_id=user_id_to_approve,
            text='🎉 <b>PRO MEMBERSHIP ACTIVATED!</b>\n\nYou now have full unlimited access to all exit exam questions.',
            parse_mode='HTML',
        )
    except Exception as e:
        await update.message.reply_text(f'Error occurred: {e}')

async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('❌ Unauthorized! Admin only.')
        return

    paid_count = get_paid_users_count()
    total_revenue = paid_count * 100
    await update.message.reply_text(
        f"📊 <b>ADMIN DASHBOARD</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• <b>Paid PRO Users:</b> {paid_count}\n"
        f"• <b>Total Revenue:</b> {total_revenue} ETB",
        parse_mode='HTML'
    )

# 4. Main Execution
if __name__ == '__main__':
    threading.Thread(target=run_flask, daemon=True).start()

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8809032194:AAGpO0DPvCW87RMj-BulJempz8dEMwciJxE")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('quiz', start_quiz))
    app.add_handler(CommandHandler('approve', approve_user))
    app.add_handler(CommandHandler('stats', admin_stats))
    app.add_handler(CallbackQueryHandler(handle_answer, pattern='^ans\|'))
    app.add_handler(CallbackQueryHandler(next_question, pattern='^next\|'))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_buttons))

    print('Bot started with updated Modern UI...')
    app.run_polling()
