import handlers
from config import dp
from aiogram import executor
import sys
import os

PATH = os.getcwd()
sys.path.append(PATH)

# from server.backend import logging

async def on_startup(dp):
    # logging.logger.info("Бот запущен")
    pass
    

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
