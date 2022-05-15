from config import dp, env
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text='new_order')
async def echo(call: CallbackQuery):
    link = env('DOCUMENT_LINK')
    await call.answer(cache_time=5)
    await call.message.answer(f'{link}', disable_web_page_preview=False)
    
@dp.callback_query_handler(text='orders')
async def echo(call: CallbackQuery):
    link = env('DOCUMENTS_LINK')
    await call.answer(cache_time=5)
    await call.message.answer(f'{link}', disable_web_page_preview=False)
