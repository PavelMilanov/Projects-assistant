from config import dp
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ContentType


@dp.message_handler()
async def echo(message: Message):
    await message.answer(f'текст: {message.text}, id: {message.from_user.id}')