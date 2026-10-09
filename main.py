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
from database import (
    init_db,
    add_paid_user,
    is_user_paid,
    get_paid_users_count,
    add_all_user,
    get_all_users,
    get_total_users_count,
)

# Initialize Database on Start
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

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton('🚀 Start'), KeyboardButton('🎯 Start Quiz')],
        [KeyboardButton('💳 Payment / Upgrade'), KeyboardButton('ℹ️ Help / Admin')],
        [KeyboardButton('🆔 My User ID')],
    ],
    resize_keyboard=True,
)

# 3. Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_all_user(user_id)  # Track user for broadcasting
    
    user_name = update.effective_user.first_name
    welcome_text = (
        f'Welcome {user_name}! 👋\n\n'
        f'Welcome to the **Computer Science Exit Exam Practice Bot**.\n\n'
        f'📌 You can practice the first {FREE_QUESTIONS_LIMIT} questions for FREE!\n'
        f'Use the buttons below to navigate and begin.'
    )
    await update.message.reply_text(
        welcome_text, reply_markup=MAIN_KEYBOARD, parse_mode='Markdown'
    )

async def start_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_all_user(update.effective_user.id)
    context.user_data['current_index'] = 0
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        index = context.user_data.get('current_index', 0)
        chat_id = update.effective_chat.id

        user_has_paid = is_user_paid(chat_id)

        if index >= FREE_QUESTIONS_LIMIT and not user_has_paid:
            payment_text = (
                f'🔒 **Free Trial Limit Reached!**\n\n'
                f'You have completed your free trial of {FREE_QUESTIONS_LIMIT} questions.\n'
                f'To unlock all questions, please pay **100 ETB**.\n\n'
                f'💳 **Payment Options:**\n'
                f'• **Telebirr / CBE:** `0934234392`\n'
                f'• **Account Name:** Kebede Assefa\n\n'
                f'📩 **Confirmation:**\n'
                f'Send your payment receipt screenshot and your User ID (`{chat_id}`) to Admin: {ADMIN_USERNAME}\n\n'
                f'Your access will be activated immediately after verification.'
            )
            await context.bot.send_message(chat_id=chat_id, text=payment_text, parse_mode='Markdown')
            return

        if index >= len(CS_EXIT_EXAM_2018):
            text = '🎉 **Congratulations! You have completed all questions.**'
            await context.bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown')
            return

        q = CS_EXIT_EXAM_2018[index]
        letters = ['A', 'B', 'C', 'D', 'E', 'F']

        keyboard = []
        for opt_idx, option in enumerate(q['options']):
            letter_prefix = letters[opt_idx] if opt_idx < len(letters) else f'{opt_idx+1}'
            button_label = f'{letter_prefix}. {option}'
            keyboard.append([InlineKeyboardButton(button_label, callback_data=f'ans|{index}|{opt_idx}')])

        reply_markup = InlineKeyboardMarkup(keyboard)
        question_text = f"**Question {q['id']} / {len(CS_EXIT_EXAM_2018)}**\n\n{q['question']}"

        await context.bot.send_message(
            chat_id=chat_id,
            text=question_text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
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
            f'✅ **Correct Answer!**\n\n'
            f"🎯 **Answer:** {q['correct_answer']}\n"
            f"💡 **Explanation:** {q['explanation']}"
        )
    else:
        result_text = (
            f'❌ **Incorrect Answer!**\n\n'
            f'Your Choice: {user_choice_formatted}\n'
            f"🎯 **Correct Answer:** {q['correct_answer']}\n\n"
            f"💡 **Explanation:** {q['explanation']}"
        )

    next_q_index = q_index + 1
    next_keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Next Question ➡️', callback_data=f'next|{next_q_index}')]]
    )

    await query.edit_message_text(text=result_text, reply_markup=next_keyboard, parse_mode='Markdown')

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
    add_all_user(user_id)

    if text in ['🚀 Start', '⚡ Main Menu']:
        await start(update, context)
    elif text in ['🎯 Start Quiz', '🎯 Quiz Start']:
        await start_quiz(update, context)
    elif text in ['💳 Payment / Upgrade', '💳 Kfya / Payment']:
        status = "✅ **Active Subscriber**" if is_user_paid(user_id) else "❌ **Free Trial User**"
        payment_info = (
            f'💳 **Payment Information**\n\n'
            f'• **Status:** {status}\n'
            f'• **Telebirr / CBE:** `0934234392`\n'
            f'• **Account Name:** Kebede Assefa\n'
            f'• **Fee:** 100 ETB\n\n'
            f'🆔 **Your Telegram User ID:** `{user_id}`\n\n'
            f'After payment, send your receipt screenshot along with your User ID to Admin: {ADMIN_USERNAME}'
        )
        await update.message.reply_text(payment_info, parse_mode='Markdown')
    elif text in ['ℹ️ Help / Admin']:
        await update.message.reply_text(f'For support or questions, contact Admin: {ADMIN_USERNAME}')
    elif text == '🆔 My User ID':
        await update.message.reply_text(
            f'👤 **Your Telegram User ID:** `{user_id}`\n\n'
            f'*(Tap the ID number above to copy it and send it to the Admin for approval.)*',
            parse_mode='Markdown'
        )

async def approve_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('❌ Unauthorized! Only Admin can use this command.')
        return

    if not context.args:
        await update.message.reply_text('⚠️ Please provide User ID! (Example: `/approve 987654321`)', parse_mode='Markdown')
        return

    try:
        user_id_to_approve = int(context.args[0])
        add_paid_user(user_id_to_approve)

        await update.message.reply_text(
            f'✅ User ID `{user_id_to_approve}` approved and saved to Database successfully!',
            parse_mode='Markdown',
        )
        await context.bot.send_message(
            chat_id=user_id_to_approve,
            text='🎉 **Payment Verified!**\n\nYou now have full access to all exit exam questions.',
            parse_mode='Markdown',
        )
    except Exception as e:
        await update.message.reply_text(f'Error occurred: {e}')

async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('❌ Unauthorized! Only Admin can use this command.')
        return

    paid_count = get_paid_users_count()
    total_users = get_total_users_count()
    total_revenue = paid_count * 100
    
    await update.message.reply_text(
        f'📊 **Admin Statistics**\n\n'
        f'• **Total Users Started Bot:** {total_users}\n'
        f'• **Total Paid Users:** {paid_count}\n'
        f'• **Total Revenue:** {total_revenue} ETB',
        parse_mode='Markdown'
    )

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """ለአስተዳዳሪ ብቻ፡ ለሁሉም ተጠቃሚዎች መልእክት መላኪያ"""
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('❌ Unauthorized! Only Admin can use this command.')
        return

    if not context.args:
        await update.message.reply_text(
            '⚠️ **Usage:** `/broadcast Your message here...`\n'
            'Example: `/broadcast Hello students! New questions are added.`',
            parse_mode='Markdown'
        )
        return

    message_to_send = " ".join(context.args)
    all_users = get_all_users()
    
    success_count = 0
    fail_count = 0

    await update.message.reply_text(f'📢 Sending message to {len(all_users)} users...')

    for uid in all_users:
        try:
            await context.bot.send_message(
                chat_id=uid,
                text=f'📢 **Announcement from Admin:**\n\n{message_to_send}',
                parse_mode='Markdown'
            )
            success_count += 1
        except Exception:
            fail_count += 1

    await update.message.reply_text(
        f'✅ **Broadcast Completed!**\n\n'
        f'• **Successfully Sent:** {success_count}\n'
        f'• **Failed/Blocked:** {fail_count}',
        parse_mode='Markdown'
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
    app.add_handler(CommandHandler('broadcast', broadcast))
    app.add_handler(CallbackQueryHandler(handle_answer, pattern='^ans\|'))
    app.add_handler(CallbackQueryHandler(next_question, pattern='^next\|'))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_buttons))

    print('Bot started successfully with Broadcast support...')
    app.run_polling()
