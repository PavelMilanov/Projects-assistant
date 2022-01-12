from pymongo import MongoClient


client = MongoClient('localhost', 27017)
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
    def insert_files(item: dict):
        try:
            db.files.insert_one(item)  # insert_meny()
            return 'запись создана'
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
    def update(old_document: dict, new_document: dict):
        try:
            return db.tokens.update_one(old_document, new_document)
        except Exception as e:
            return f'ошибка: {e}'

    @staticmethod
    def delete_token(request: dict):
        try:
            db.tokens.delete_one(request)
        except Exception as e:
            return f'ошибка: {e}'
        
    @staticmethod
    def delete_file(request: dict):
        try:
            db.files.delete_one(request)
        except Exception as e:
            return f'ошибка: {e}'
