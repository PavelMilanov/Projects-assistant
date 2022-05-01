from pymongo import MongoClient
from environs import Env


env = Env()
env.read_env()

client = MongoClient(f"mongo+srv://{env('DB_USERNAME')}:{env('DB_PASSWORD')}@mongodb")
db = client['main']


class Database:

    @staticmethod
    def insert_tokens(item: dict):
        try:
            db.tokens.insert_one(item)  # insert_meny()
            return 'запись создана'
        except Exception as e:
            return f'ошибка: {e}'
        
    @staticmethod
    def insert_files(item1: dict):
        try:
            db.files.insert_one(item1)
            return 'запись обновлена'
        except Exception as e:
            return f'ошибка: {e}'
    

    @staticmethod
    def find_all_files():
        try:
            return db.files.find()
        except Exception as e:
            pass

    @staticmethod
    def find_tokens(request: dict):
        try:
            return db.tokens.find_one(request)
        except Exception as e:
            return f'ошибка: {e}'
        
    @staticmethod
    def find_file(request: dict):
        try:
            return db.files.find_one(request)
        except Exception as e:
            return f'ошибка: {e}'

    @staticmethod
    def delete_token(request: dict):
        try:
            db.tokens.delete_one(request)
        except Exception as e:
            return f'ошибка: {e}'
        
    @staticmethod
    def delete_file():
        try:
            db.files.drop()
        except Exception as e:
            return f'ошибка: {e}'
