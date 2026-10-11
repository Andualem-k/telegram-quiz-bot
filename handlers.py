from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from mgmt_questions import (
    MGMT_2016, MGMT_M2016,
    MGMT_2017, MGMT_M2017,
    MGMT_2018, MGMT_M2018
)
from cs_questions import CS_EXIT_EXAM_2018
from it_questions import IT_EXIT_EXAM

# 1. ዲፓርትመንት ሲመረጥ የዓመታት ምናሌ የሚያሳይ
async def show_years_menu(update, context, dept_code):
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
    
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode='Markdown')
    else:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode='Markdown')

# 2. ተማሪው ዓመቱን ሲመርጥ ጥያቄውን የሚጭን እና ወደ መጀመሪያው ጥያቄ የሚያልፍ
async def handle_exam_selection(update, context):
    query = update.callback_query
    await query.answer()
    
    data = query.data  # ምሳሌ: 'mgmt_2017' ወይም 'mgmt_m2016'
    try:
        dept, exam_type = data.split('_', 1)
    except ValueError:
        return
    
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
        
    context.user_data['department'] = dept
    context.user_data['questions_list'] = selected_questions
    context.user_data['current_index'] = 0
    
    exam_title = f"Exit Exam {exam_type}" if not exam_type.startswith('m') else f"Model Exam {exam_type[1:]}"
    await query.edit_message_text(f"✅ **{dept.upper()} - {exam_title}** ተመርጧል! ፈተናው ይጀምራል...", parse_mode='Markdown')
    
    # ከ main.py ውስጥ ያለውን send_question መጥራት እንዲቻል ወይም በቀጥታ ማሳየት
    from main import send_question
    await send_question(update, context)
