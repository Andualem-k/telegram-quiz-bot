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

# ጥያቄዎችን እና Database መጫን
from cs_questions import CS_EXIT_EXAM_2018
from mgmt_questions import (
    MGMT_2016, MGMT_M2016,
    MGMT_2017, MGMT_M2017,
    MGMT_2018, MGMT_M2018
)
from it_questions import IT_EXIT_EXAM
from database import (
    init_db,
    add_paid_user,
    is_user_paid,
    get_paid_users_count,
    add_all_user,
    get_all_users,
    get_total_users_count,
)

# Database ማስመርመር
init_db()

# 1. Render Web Service እንዲሰራ Flask መክፈት
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Quiz Bot is alive and running!", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

# 2. Logging ማስተካከል
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

FREE_QUESTIONS_LIMIT = 5
ADMIN_ID = 1519242710
ADMIN_USERNAME = '@anmg2828kt'

MAIN_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton('💻 CS Exam'), KeyboardButton('🌐 IT Exam')],
        [KeyboardButton('📊 Marketing Mgmt')],
        [KeyboardButton('💳 Payment / Upgrade'), KeyboardButton('ℹ️ Help / Admin')],
        [KeyboardButton('🆔 My User ID'), KeyboardButton('🔗 Share Bot')],
    ],
    resize_keyboard=True,
)

def get_questions_for_user(context: ContextTypes.DEFAULT_TYPE):
    if 'questions_list' in context.user_data and context.user_data['questions_list']:
        return context.user_data['questions_list']
    return CS_EXIT_EXAM_2018

# 3. Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_all_user(user_id)
    
    user_name = update.effective_user.first_name
    welcome_text = (
        f"Welcome {user_name}! 👋\n\n"
        f"Welcome to the **Ethiopian University Exit Exam Practice Bot**.\n\n"
        f"📚 **Available Departments:**\n"
        f"1. 💻 **Computer Science (CS)**\n"
        f"2. 🌐 **Information Technology (IT)**\n"
        f"3. 📊 **Marketing Management**\n\n"
        f"📌 You can practice the first {FREE_QUESTIONS_LIMIT} questions for FREE in each department!\n"
        f"Choose your department below to begin."
    )
    await update.message.reply_text(
        welcome_text, reply_markup=MAIN_KEYBOARD, parse_mode='Markdown'
    )

# ዲፓርትመንት ሲመረጥ የዓመታት ምናሌ ማሳያ
async def show_years_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, dept_code: str):
    add_all_user(update.effective_user.id)
    context.user_data['department'] = dept_code
    
    dept_titles = {
        'cs': 'Computer Science (CS)',
        'it': 'Information Technology (IT)',
        'mgmt': 'Marketing Management'
    }
    
    keyboard = [
        [
            InlineKeyboardButton("📄 Exit Exam 2016", callback_data=f"{dept_code}_2016"),
            InlineKeyboardButton("📝 Model 2016", callback_data=f"{dept_code}_m2016")
        ],
        [
            InlineKeyboardButton("📄 Exit Exam 2017", callback_data=f"{dept_code}_2017"),
            InlineKeyboardButton("📝 Model 2017", callback_data=f"{dept_code}_m2017")
        ],
        [
            InlineKeyboardButton("📄 Exit Exam 2018", callback_data=f"{dept_code}_2018"),
            InlineKeyboardButton("📝 Model 2018", callback_data=f"{dept_code}_m2018")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = f"📚 **{dept_titles.get(dept_code, '')}**\n\nእባክዎ የሚፈልጉትን የፈተና ዓመት ወይም የሞዴል ፈተና ይምረጡ፡"
    
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# ተማሪው ዓመቱን ወይም ሞዴሉን ሲመርጥ የሚሰራ
async def handle_exam_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data  # ምሳሌ: 'mgmt_2017'
    try:
        dept, exam_type = data.split('_', 1)
    except ValueError:
        return

    context.user_data['department'] = dept
    context.user_data['current_index'] = 0

    selected_questions = []

    if dept == 'mgmt':
        if exam_type == '2016':
            selected_questions = MGMT_2016
        elif exam_type == 'm2016':
            selected_questions = MGMT_M2016
        elif exam_type == '2017':
            selected_questions = MGMT_2017
        elif exam_type == 'm2017':
            selected_questions = MGMT_M2017
        elif exam_type == '2018':
            selected_questions = MGMT_2018
        elif exam_type == 'm2018':
            selected_questions = MGMT_M2018
        else:
            selected_questions = MGMT_2017
    elif dept == 'it':
        selected_questions = IT_EXIT_EXAM
    elif dept == 'cs':
        selected_questions = CS_EXIT_EXAM_2018

    if not selected_questions:
        await query.edit_message_text("⚠️ የዚህ ዓመት ጥያቄዎች በቅርቡ ይጫናሉ! እባክዎ ሌላ ይምረጡ።", parse_mode='Markdown')
        return

    context.user_data['questions_list'] = selected_questions

    # የድሮውን ምናሌ መልዕክት ማፅዳት
    try:
        await query.delete_message()
    except Exception:
        pass

    # ጥያቄውን መላክ
    await send_question(update, context)

async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        index = context.user_data.get('current_index', 0)
        chat_id = update.effective_chat.id

        user_has_paid = is_user_paid(chat_id)
        questions_list = get_questions_for_user(context)

        if index >= FREE_QUESTIONS_LIMIT and not user_has_paid:
            payment_text = (
                f'🔒 **Free Trial Limit Reached!**\n\n'
                f'You have completed your free trial of {FREE_QUESTIONS_LIMIT} questions.\n'
                f'To unlock all questions across all departments, please pay **100 ETB**.\n\n'
                f'💳 **Payment Options:**\n'
                f'• **Telebirr / CBE:** `0934234392`\n'
                f'• **Account Name:** Kebede Assefa\n\n'
                f'📩 **Confirmation:**\n'
                f'Send your payment receipt screenshot and your User ID (`{chat_id}`) to Admin: {ADMIN_USERNAME}\n\n'
                f'Your access will be activated immediately after verification.'
            )
            await context.bot.send_message(chat_id=chat_id, text=payment_text, parse_mode='Markdown')
            return

        if index >= len(questions_list):
            text = '🎉 **Congratulations! You have completed all questions in this department/year.**'
            await context.bot.send_message(chat_id=chat_id, text=text, parse_mode='Markdown')
            return

        q = questions_list[index]
        letters = ['A', 'B', 'C', 'D', 'E', 'F']

        keyboard = []
        for opt_idx, option in enumerate(q['options']):
            letter_prefix = letters[opt_idx] if opt_idx < len(letters) else f'{opt_idx+1}'
            button_label = f'{letter_prefix}. {option}'
            keyboard.append([InlineKeyboardButton(button_label, callback_data=f'ans|{index}|{opt_idx}')])

        reply_markup = InlineKeyboardMarkup(keyboard)
        
        dept_code = context.user_data.get('department')
        dept_title = "Information Technology" if dept_code == 'it' else ("Marketing Management" if dept_code == 'mgmt' else "Computer Science")
        
        question_text = f"📚 **{dept_title}**\n**Question {q.get('id', index+1)} / {len(questions_list)}**\n\n{q['question']}"

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

    questions_list = get_questions_for_user(context)

    if q_index >= len(questions_list):
        return

    q = questions_list[q_index]
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
    elif text in ['💻 CS Exam', '💻 Computer Science']:
        await show_years_menu(update, context, 'cs')
    elif text in ['🌐 IT Exam', '🌐 Information Technology']:
        await show_years_menu(update, context, 'it')
    elif text in ['📊 Marketing Mgmt', '📊 Marketing Management']:
        await show_years_menu(update, context, 'mgmt')
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
    elif text == '🔗 Share Bot':
        share_msg = (
            "🎓 **Exit Exam መለማመጃ ቦት!**\n\n"
            "በ Computer Science፣ IT እና Marketing Management የተዘጋጁ የ Exit Exam ጥያቄዎችን ከነማብራሪያቸው ይለማመዱ።\n\n"
            "👇 አሁኑኑ ለመጀመር ከታች ያለውን ሊንክ ይጫኑ፦\n"
            "https://t.me/ethio_exit_exam_quiz_bot"
        )
        await update.message.reply_text(
            f"የሚከተለውን መልዕክት ፎርዋርድ በማድረግ ወይም ኮፒ በማድረግ ለጓደኞችዎ እና ለግሩፖች ያጋሩ፦\n\n{share_msg}"
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
            text='🎉 **Payment Verified!**\n\nYou now have full access to all exit exam questions across all departments.',
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
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text('❌ Unauthorized! Only Admin can use this command.')
        return

    if not context.args:
        await update.message.reply_text(
            '⚠️ **Usage:** `/broadcast Your message here...`\n'
            'Example: `/broadcast Hello students! New IT questions are added.`',
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
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8809032194:AAGpO0DPvCW87RMj-BulJempz8dEMwciJxE")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('approve', approve_user))
    app.add_handler(CommandHandler('stats', admin_stats))
    app.add_handler(CommandHandler('broadcast', broadcast))
    
    # የዓመታት እና ሞዴል ምርጫ Handler
    app.add_handler(CallbackQueryHandler(handle_exam_selection, pattern=r'^(cs|it|mgmt)_(2016|2017|2018|m2016|m2017|m2018)\$'))
    
    app.add_handler(CallbackQueryHandler(handle_answer, pattern=r'^ans\|'))
    app.add_handler(CallbackQueryHandler(next_question, pattern=r'^next\|'))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_buttons))

    print('Bot started successfully with Year Sub-menus support...')
    app.run_polling()
