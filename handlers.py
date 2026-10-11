from mgmt_questions import MGMT_2017
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from mgmt_questions import MGMT_2017

# 1. ዲፓርትመንት ሲመረጥ የዓመታት ምናሌ የሚያሳይ
async def show_years_menu(update, context, dept_code):
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
    text = "እባክዎ የሚፈልጉትን የፈተና ዓመት ወይም የሞዴል ፈተና ይምረጡ፡"
    
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text, reply_markup=reply_markup)

# 2. ተማሪው ዓመቱን ሲመርጥ ጥያቄውን የሚጭን
async def handle_exam_selection(update, context):
    query = update.callback_query
    data = query.data  # ለምሳሌ: 'mgmt_2017'
    
    dept, exam_type = data.split('_')
    selected_questions = []
    
    if dept == 'mgmt' and exam_type == '2017':
        selected_questions = MGMT_2017
        
    if not selected_questions:
        await query.answer("⚠️ የዚህ ዓመት ጥያቄዎች በቅርቡ ይጫናሉ! እባክዎ ሌላ ይምረጡ።", show_alert=True)
        return
        
    context.user_data['questions'] = selected_questions
    context.user_data['current_q_index'] = 0
    context.user_data['score'] = 0
    await query.answer()
