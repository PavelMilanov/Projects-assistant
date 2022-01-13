from config import dp, bot
from aiogram.types import Message, CallbackQuery


@dp.message_handler()
async def echo(message: Message):
    await message.answer(f'ответ: {message.text} в чате {message.chat.id}')
