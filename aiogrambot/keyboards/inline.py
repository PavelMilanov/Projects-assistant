from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def report(callback_data_text):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='Посмотреть' , callback_data=f'{callback_data_text}')
    return keyboard.add(button1)
    