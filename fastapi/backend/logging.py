from loguru import logger
import sys
import os

PATH = os.getcwd()
sys.path.append(PATH)

logger.add(f'{PATH}/debug/logs.log', format='{time} {level} {message}',
    level='DEBUG', rotation='100 KB',
    compression='zip')
