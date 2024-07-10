from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    ContextTypes, 
    ConversationHandler,
)
from telegram.constants import ParseMode


from .functions import keyboard, make_buttons
from .config import logger
from .list import main_menu, first_button
from config.db import db



FIRST_NAME, LAST_NAME, FATHER_NAME, DATA_BIRTH, GENDER, PHONE_NUMBER, INSURANCE_NAME, INSURANCE_NUMBER, RANGE, EDIT_PROFILE = range(10)
CLINIC_NUMBER, DOC_SPEC, DATA = range(3)

convers_button = ['Ошибка', '#','/cancel']

async def first_step(update, context):
    print('first')
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Для отмены введите /cancel\n\nВведите ваше имя:", 
                                reply_markup=await keyboard(convers_button))
    return FIRST_NAME


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    all_ids = db.get_all_user_ids()

    if update.effective_user.id not in all_ids:
        button = main_menu
    else:
        button = first_button

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Вы вышли из формы",
                                reply_markup=ReplyKeyboardRemove())
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Меню",
                                reply_markup=await make_buttons(button))
    return ConversationHandler.END


async def second_step(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data['first_name'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Проверьте ваше имя: <b>{context.user_data['first_name']}</b>\n\n"
                                "Если допущена ошибка введите слово <b>Ошибка</b>, "
                                "если все указано верно то введите фамилию\n\n"
                                "Введите вашу фамилию: ", 
                                parse_mode=ParseMode.HTML,
                                reply_markup=await keyboard(convers_button))
    return LAST_NAME


async def third_step(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.lower() == 'ошибка':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Введите ваше имя: ", 
                                reply_markup=await keyboard(convers_button))
        return FIRST_NAME

    context.user_data['last_name'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Проверьте вашу фамилию: <b>{context.user_data['last_name']}</b>\n\n"
                                "Eсли допущена ошибка введите слово <b>Ошибка</b>, "
                                "если все указано верно то введите отчество\n\n"
                                "Введите ваше отчество: ", 
                                parse_mode=ParseMode.HTML,
                                reply_markup=await keyboard(convers_button))
    return FATHER_NAME

async def fourth_step(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.lower() == 'ошибка':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Введите вашу фамилию: ", 
                                reply_markup=await keyboard(convers_button))
        return LAST_NAME

    context.user_data['father_name'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Проверьте ваше отчество: <b>{context.user_data['father_name']}</b>\n\n"
                                "Eсли допущена ошибка введите слово <b>Ошибка</b>, "
                                "если все указано верно то введите дату рождения\n\n"
                                "Введите дату рождения в формате 'дд.мм.гггг': ", 
                                parse_mode=ParseMode.HTML,
                                reply_markup=await keyboard(convers_button))
    return DATA_BIRTH

async def fourth_new_step(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.lower() == 'ошибка':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Введите ваше отчество: ", 
                                reply_markup=await keyboard(convers_button))
        return FATHER_NAME
    
    import re
    pattern = r'^\d{2}\.\d{2}\.\d{4}$'
    if re.match(pattern, update.message.text) == None:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Пожалуйста введите дату рождения в формате 'дд.мм.гггг', \n"
                                "например: 12.12.1988", 
                                reply_markup=await keyboard(convers_button))
        return DATA_BIRTH
    
    context.user_data['data_birth'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Проверьте вашу дату рождения: <b>{context.user_data['data_birth']}</b>\n\n"
                                "Eсли допущена ошибка введите слово <b>Ошибка</b>, "
                                "если все указано верно то выберите пол\n\n"
                                "Ваш пол: ", 
                                parse_mode=ParseMode.HTML,
                                reply_markup=await keyboard(
                                    ['Мужчина', '#','Женщина', '#'] + convers_button
                                ))
    return GENDER

async def fourth_new2_step(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.lower() == 'ошибка':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Пожалуйста введите дату рождения в формате 'дд.мм.гггг', \n"
                                "например: 12.12.1988", 
                                reply_markup=await keyboard(convers_button))
        return DATA_BIRTH
    
    if update.message.text.lower() != 'мужчина' and update.message.text.lower() != 'женщина':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Допущена ошибка, выберите между <b>'Мужчина'</b> и <b>'Женщина'</b>", 
                                parse_mode=ParseMode.HTML,
                                reply_markup=await keyboard(
                                    ['Мужчина', '#','Женщина', '#'] + convers_button
                                ))
        return GENDER

    context.user_data['gender'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Проверьте ваш пол: <b>{context.user_data['gender']}</b>\n\n"
                                "Eсли допущена ошибка введите слово <b>Ошибка</b>, "
                                "если все указано верно то введите ваш номер телефона\n\n"
                                "Введите ваш номер телефона: ", 
                                parse_mode=ParseMode.HTML,
                                reply_markup=await keyboard(convers_button))
    return PHONE_NUMBER


async def fifth_step(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.lower() == 'ошибка':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Выберите ваш пол: ", 
                                reply_markup=await keyboard(
                                    ['Мужчина', '#','Женщина', '#'] + convers_button
                                ))
        return GENDER
    
    if not update.message.text.isdigit() or 10 >= len(update.message.text) or 13 <= len(update.message.text):
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                            text="Повторите ввод номера телефона в формате 89997776666, используйте только цифры:")
        return PHONE_NUMBER

    context.user_data['phone_number'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Проверьте ваш номер телефона: <b>{context.user_data['phone_number']}</b>\n\n"
                                "Eсли допущена ошибка введите слово <b>Ошибка</b>, "
                                "если все указано верно то введите название вашей страховой компании\n\n"
                                "Введите название вашей страховой компании: ", 
                                parse_mode=ParseMode.HTML,
                                reply_markup=await keyboard(convers_button))
    return INSURANCE_NAME

async def fifth_new_step(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.lower() == 'ошибка':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Введите ваш номер телефона: ", 
                                reply_markup=await keyboard(convers_button))
        return PHONE_NUMBER

    context.user_data['insurance_name'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Проверьте название вашей страховой: <b>{context.user_data['insurance_name']}</b>\n\n"
                                "Eсли допущена ошибка введите слово <b>Ошибка</b>, "
                                "если все указано верно то введите номер полиса\n\n"
                                "Введите номер полиса ДМС, 16 цифр: ",
                                parse_mode=ParseMode.HTML, 
                                reply_markup=await keyboard(convers_button))
    return INSURANCE_NUMBER

async def six_step(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.text.lower() == 'ошибка':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Введите название вашей страховой компании: ", 
                                reply_markup=await keyboard(convers_button))
        return INSURANCE_NAME
    
    if not update.message.text.isdigit() or 15 >= len(update.message.text) or 17 <= len(update.message.text):
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                            text="Повторите ввод номера вашего полиса ДМС, должно быть 16 цифр:")
        return INSURANCE_NUMBER

    context.user_data['insurance_number'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Проверьте номер вашего полиса ДМС: <b>{context.user_data['insurance_number']}</b>\n\n"
                                "Eсли допущена ошибка введите слово <b>Ошибка</b>, "
                                "если все указано верно то введите <b>Готово</b>",
                                parse_mode=ParseMode.HTML, 
                                reply_markup=await keyboard(['Готово', '#'] + convers_button))
    return RANGE


async def final_functions(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    if update.message.text.lower() == 'ошибка':
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Введите номер вашего полиса ДМС: ", 
                                reply_markup=await keyboard(convers_button))
        return INSURANCE_NUMBER
    
    from datetime import datetime

    user_id = update.effective_user.id
    username = update.effective_user.username
    first_name = context.user_data['first_name']
    last_name = context.user_data['last_name']
    father_name = context.user_data['father_name']
    phone_number = context.user_data['phone_number']
    data_birth = context.user_data['data_birth']

    insurance_name = context.user_data['insurance_name']
    insurance_number = context.user_data['insurance_number']
    gender = 0
    if context.user_data['gender'] == 'Мужчина':
        gender = 1

    reg_date = datetime.today().strftime('%d.%m.%Y')

    db.add_user([user_id, username, first_name, last_name,
            father_name, phone_number, insurance_number, reg_date, 
            gender, insurance_name, data_birth])
    

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Вы были успешно зарегестрированы ✅",
                                reply_markup=ReplyKeyboardRemove())
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Главное меню 🗂",
                                reply_markup=await make_buttons(main_menu))
    
    return ConversationHandler.END


colum = {
    'edit--last-name': ['фамилии', 'last-name'], 
    'edit--first-name': ['имени', 'first_name'],
    'edit--father-name': ['отчества', 'father_name'],
    'edit--phone': ['номера телефона', 'phone_number'],
    'edit--insurence': ['полиса ДМС', 'insurance_number'],
    'edit--gender': ['вашего пола', 'gender'],
}



async def edit_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('edit')
    context.user_data['callback'] = update.callback_query.data

    button = None
    if context.user_data['callback'] == 'edit--gender':
        button = await keyboard(['Мужчина', '#','Женщина'])

    await context.bot.send_message(chat_id=update.effective_chat.id,
                            text=f'Введите новое значение для {colum[update.callback_query.data][0]}', 
                            reply_markup=button)
    return EDIT_PROFILE

async def edit_profile2(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if context.user_data['callback'] == 'edit--phone':
        if not update.message.text.isdigit() or 10 >= len(update.message.text) or 13 <= len(update.message.text):
            await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Повторите ввод номера телефона в формате 89997776666, используйте только цифры:")
            return EDIT_PROFILE
    
    elif context.user_data['callback'] == 'edit--insurence':
        if not update.message.text.isdigit() or 15 >= len(update.message.text) or 17 <= len(update.message.text):
            await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text="Повторите ввод номера вашего полиса ДМС, должно быть 16 цифр:")
            return EDIT_PROFILE

    user_id = update.effective_user.id
    value = update.message.text

    if context.user_data['callback'] == 'edit--gender':
        value = 0
        if update.message.text == 'Мужчина':
            value = 1 
    
    db.update_by_id(user_id, value, colum[context.user_data['callback']][1])

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Данные для вашего {colum[context.user_data['callback']][0]} "
                                f"успешно изменены на <b>{value}</b> ✅",
                                parse_mode=ParseMode.HTML, 
                                reply_markup=await make_buttons([
                                    ('Вернуться к настройкам ↪️', 'edit-prof'),
                                    ('', '#'),
                                    ('', '#'),
                                    ('В главное меню 🗂', 'main-menu'),
                                ]))
    return ConversationHandler.END



async def make_record(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('record')
    await context.bot.send_message(chat_id=update.effective_chat.id,
                            text=f'Здесь будет предложино выбрать клинику\n\n'
                            'Введите номер телефона для теста в формате 79998887722:', 
                            reply_markup=None)
    return CLINIC_NUMBER

async def make_record2(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message.text.isdigit() or 10 >= len(update.message.text) or 13 <= len(update.message.text):
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                            text="Повторите ввод номера телефона в формате 79998887722, используйте только цифры:")
        return CLINIC_NUMBER
    
    context.user_data['request_phone'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Здесь будет предложено к какому врачу записаться\n\n"
                                "Введите специальность врача (лор, терапевт, окулист...):",
                                parse_mode=ParseMode.HTML, 
                                reply_markup=await make_buttons([
                                    ('В главное меню 🗂', 'main-menu'),
                                ]))
    return DOC_SPEC

async def make_record3(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data['doc_spec'] = update.message.text

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Здесь будет предложено выбрать дату\n\n"
                                "Для теста введите дату и время в формате '21.06.24 в 10:00':",
                                parse_mode=ParseMode.HTML, 
                                reply_markup=await make_buttons([
                                    ('В главное меню 🗂', 'main-menu'),
                                ]))
    return DATA

async def make_record4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from zvonobot.call_requests import make_call

    apiKey = '#'

    phone = context.user_data['request_phone']
    doctor = context.user_data['doc_spec']
    comfort_date = update.message.text

    user_id = update.effective_user.id

    result = db.get_user_by_id(user_id)
    print(f'{result=}')

    full_name = f'{result[4]} {result[3]} {result[5]}'
    data_birth = result[6]
    gender = result[10]
    my_phone = result[7]
    insurance_name = result[8]
    insurance_number = result[9]

    data_dict = make_call(
        apiKey, phone, gender,
        doctor, full_name, data_birth,
        insurance_name, insurance_number,
        comfort_date, my_phone, user_id
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f"Совершается звонок, по окончанию вам придёт ответ с результатом",
                                parse_mode=ParseMode.HTML, 
                                reply_markup=await make_buttons([
                                    ('В главное меню 🗂', 'main-menu'),
                                ]))
    return ConversationHandler.END

