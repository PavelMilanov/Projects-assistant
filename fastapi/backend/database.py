from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['Main']


class Database:

    @staticmethod
    def insert(item: dict):
        try:
            db.tokens.insert_one(item)  # insert_meny()
            return 'запись создана'
        except Exception as e:
            return f'ошибка: {e}'

    @staticmethod
    def find_all_collections():
        try:
            return db.tokens.find()
        except Exception as e:
            pass

    @staticmethod
    def find(request: dict):
        try:
            return db.tokens.find_one(request)
        except Exception as e:
            return f'ошибка: {e}'

    @staticmethod
    def update(old_document: dict, new_document: dict):
        try:
            return db.tokens.update_one(old_document, new_document)
        except Exception as e:
            return f'ошибка: {e}'

    @staticmethod
    def delete(request: dict):
        try:
            db.tokens.delete_one(request)
        except Exception as e:
            return f'ошибка: {e}'
