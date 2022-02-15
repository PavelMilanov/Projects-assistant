from config import bot, env, dp
from utils.tasks import scheduler
from aiogram.types import Message
from aiogram import types
from keyboards.inline import report


@scheduler.scheduled_job('cron', day_of_week='mon', hour='20', id='1')
async def report_generated_order():
    user1 = env.list('ADMINS')[0]
    user2 = env.list('ADMINS')[2]
    await bot.send_message(chat_id=user1, text=f'сгенерирован новый отчет', reply_markup=report('new_order'))
    await bot.send_message(chat_id=user2, text=f'сгенерирован новый отчет', reply_markup=report('new_order'))
    
@scheduler.scheduled_job('cron', day_of_week='tue', hour='15', minute='2', id='2')
async def report_generated_order():
    user = env.list('ADMINS')[1]
    await bot.send_message(chat_id=user, text=f'отчет сформирован и загружен в архив', reply_markup=report('orders'))
    
@dp.message_handler(commands='start')
async def get_menu(message: Message):
    await message.answer(f'Добро пожаловать, {message.from_user.full_name}.\nЯ буду присылать тебе ссылки на отчеты каждую неделю или по нажатию кнопки сбоку поля ввода.\nХорошего дня)')

@dp.message_handler(commands="set_commands", state="*", user_id=env.list('ADMINS')[0])
async def cmd_set_commands(message: Message):
    commands = [types.BotCommand(command="/last_order", description="Посмотреть последний отчет"),
    types.BotCommand(command="/full_orders", description="Посмотреть архив отчетов")
    ]
    await bot.set_my_commands(commands)
    await message.answer('Изменения внесены')
    
@dp.message_handler(commands='last_order')
async def get_menu(message: Message):
    link = env('DOCUMENT_LINK')
    await message.answer(f'Последний отчет:\n{link}')

@dp.message_handler(commands='full_orders')
async def get_menu(message: Message):
    link = env('FOLDER_LINK')
    await message.answer(f'Goole Drive папка:\n{link}')
