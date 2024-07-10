from telegram import Update, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder, 
    ContextTypes, 
    CommandHandler, 
    MessageHandler, 
    filters, 
    InlineQueryHandler, 
    CallbackContext, 
    CallbackQueryHandler,
    ConversationHandler
)
from telegram.constants import ParseMode

from config.config import TOKEN, logger
from config.functions import make_buttons, keyboard
from config.list import main_menu, first_button, gender_list
from config.converstation import *
from config.db import db

import os



application = ApplicationBuilder().token(TOKEN).build()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.chat.type != 'private':
        return

    all_ids = db.get_all_user_ids()
    first_name = update.effective_user.first_name

    if update.effective_user.id not in all_ids:

        return await context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text=f'Добро пожаловать, <b>{first_name}</b> 👋\n'
                                    'Через данный бот можно записаться на прием в ЛПУ', 
                                    parse_mode=ParseMode.HTML,
                                    reply_markup=await make_buttons(first_button))
    
    return await context.bot.send_message(chat_id=update.effective_chat.id, 
                                text=f'Здравствуйте <b>{first_name}</b> 👋\nГлавное меню 🗂', 
                                parse_mode=ParseMode.HTML,
                                reply_markup=await make_buttons(main_menu))


async def callback_handler(update: Update, context: CallbackContext):

    if update.effective_chat.type != 'private':
        return

    callback_data = update.callback_query.data
    call = update.callback_query
    user_id = update.effective_user.id
    all_ids = db.get_all_user_ids()

    if callback_data == 'main-menu':
        if user_id not in all_ids:

            return await context.bot.send_message(chat_id=update.effective_chat.id, 
                                        text='Через данный бот можно записаться на прием в ЛПУ\n'
                                        '❗️Для использования необходимо зарегестрироваться❗️', 
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=await make_buttons(first_button))
        await context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                                            message_id=call.message.message_id,
                                text='Главное меню 🗂', 
                                reply_markup=await make_buttons(main_menu))

    elif callback_data == 'about':
        await context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                                            message_id=call.message.message_id,
                                text='📑 Здесь будет описание', 
                                    parse_mode=ParseMode.HTML,
                                reply_markup=await make_buttons([('Назад ↪️', 'main-menu')]))


    ###################### profile ######################    
    elif callback_data == 'my_cabinet':
        button = [
            ('Редактировать 🖍', 'edit-prof'),
            ('', '#'),
            ('', '#'),
            ('Назад ↪️', 'main-menu'),
        ]
        result = db.get_user_by_id(user_id)
        print(f'{result=}')
        await context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                                            message_id=call.message.message_id,
                                text='Личный кабинет 🪪\n\n'
                                f'🔸 Фамилия: <b>{result[4]}</b>\n'
                                f'🔸 Имя:  <b>{result[3]}</b>\n'
                                f'🔸 Отчество: <b>{result[5]}</b>\n\n'
                                f'🔸 Пол: <b>{gender_list[result[10]]}</b>'
                                f'🔹 Дата рождения: <b>{result[6]}</b>\n'
                                f'🔹 Номер телефона: <b>{result[7]}</b>\n\n'
                                f'🔺 ДМС: <b>{result[9]}</b>\n'
                                f'🔺 Название страховой: <b>{result[8]}</b>\n\n'
                                f'Дата регистрации: <b>{result[11]}</b>', 
                                    parse_mode=ParseMode.HTML,
                                reply_markup=await make_buttons(button))
    

    elif callback_data == 'edit-prof':
        button = [
            ('Фамилию', 'edit--last-name'),
            ('', '#'),
            ('', '#'),
            ('Имя', 'edit--first-name'),
            ('', '#'),
            ('', '#'),
            ('Отчество', 'edit--father-name'),
            ('', '#'),
            ('', '#'),
            ('Номер телефона', 'edit--phone'),
            ('', '#'),
            ('', '#'),
            ('Номер ДМС', 'edit--insurence'),
            ('', '#'),
            ('', '#'),
            ('Пол', 'edit--gender'),
            ('', '#'),
            ('', '#'),
            ('Назад ↪️', 'my_cabinet'),
        ]

        await context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                                            message_id=call.message.message_id,
                                text='Что хотите отредактировать? 🖍', 
                                reply_markup=await make_buttons(button))
        
    elif callback_data == 'my_records':
        await context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                                            message_id=call.message.message_id,
                                text='📆 Здесь будут отображаться записи клиента', 
                                reply_markup=await make_buttons([('Назад ↪️', 'main-menu')]))
        
    elif callback_data == 'another-ininsurence':
        await context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                                            message_id=call.message.message_id,
                                text='📝 Нужна информация для заполнения этого раздела, '
                                'какие данные запрашивать, куда их отправлять и тд', 
                                reply_markup=await make_buttons([('Назад ↪️', 'main-menu')]))
    
    elif callback_data == 'start_record':
        await context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                                            message_id=call.message.message_id,
                                text='☎️ Здесь будет подключение через АПИ', 
                                reply_markup=await make_buttons([('Назад ↪️', 'main-menu')]))
    ###################### registration ######################
    elif callback_data == 'rulse_agree':
        logger.info('rulse_agree')
        button = [
            ('Даю согласие на обработку ✅', 'starts'),
            ('', '#'),
            ('', '#'),
            ('Не даю согласие ❌', 'not_agree'),
        ]
        logger.info('message')
        await context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text='Cейчас будет несколько вопросов о Вас!\nПросим внести '
                                    'достоверную информацию, так как эти данные будут необходимы '
                                    'нам для записи в клинику\n\n❗️Необходимо ваше согласие '
                                    'на обработку персональных данных❗️', 
                                reply_markup=await make_buttons(button))
    
    elif callback_data == 'not_agree':
        await context.bot.edit_message_text(chat_id=update.effective_chat.id, 
                                    message_id=call.message.message_id, 
                                    text='Вы не дали согласие на обработку персональных данных\n'
                                    'Регистрация прервана', 
                                reply_markup=await make_buttons(first_button))
    else:
        logger.error(f'{callback_data=}')




def main():
    start_handler = CommandHandler('start', start)

    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(first_step , pattern='^starts$')],
        states={
            FIRST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_step)],
            LAST_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, third_step)],
            FATHER_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, fourth_step)],
            DATA_BIRTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, fourth_new_step)],
            GENDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, fourth_new2_step)],
            PHONE_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, fifth_step)],
            INSURANCE_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, fifth_new_step)],
            INSURANCE_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, six_step)],
            RANGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, final_functions)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler_edit = ConversationHandler(
        entry_points=[CallbackQueryHandler(edit_profile, pattern='^edit--')],
        states={
            EDIT_PROFILE: [MessageHandler(filters.TEXT & ~filters.COMMAND, edit_profile2)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler_make_record = ConversationHandler(
        entry_points=[CallbackQueryHandler(make_record, pattern='^start_record$')],
        states={
            CLINIC_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, make_record2)],
            DOC_SPEC: [MessageHandler(filters.TEXT & ~filters.COMMAND, make_record3)],
            DATA: [MessageHandler(filters.TEXT & ~filters.COMMAND, make_record4)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )
    call_back_query = CallbackQueryHandler(callback_handler)

    
    application.add_handler(start_handler)
    application.add_handler(conv_handler)
    application.add_handler(conv_handler_edit)
    application.add_handler(conv_handler_make_record)
    application.add_handler(call_back_query)

    application.run_polling()

if __name__ == '__main__':
    main()