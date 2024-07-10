import sqlite3
from .config import logger, DATABASE_NAME

class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.Connection(db_name)
        self.cursor = self.connection
        self.create_db()
    
    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS users ("
                    "id INTEGER PRIMARY KEY, "
                    "user_id BIGINT, "
                    "username TEXT, "
                    "first_name TEXT, "
                    "last_name TEXT, "
                    "father_name TEXT, "
                    "data_birth TEXT, "
                    "phone_number BIGINT, "
                    "insurance_name TEXT, "
                    "insurance_number BIGINT, "
                    "gender INT, "
                    "reg_date TEXT);")
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            logger.error(f'Ошибка при создании таблицы: {e}')

    def add_user(self, data_list):
        self.cursor.execute(f'INSERT INTO users ('
                            'user_id, username, first_name, last_name, father_name, '
                            'phone_number, insurance_number, reg_date, gender, '
                            'insurance_name, data_birth'
                            ') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                            (data_list[0], data_list[1], data_list[2], data_list[3],
                            data_list[4], data_list[5], data_list[6], data_list[7],
                            data_list[8], data_list[9], data_list[10]))
        self.connection.commit()

    def get_all_user_ids(self):
        try:
            rows = self.cursor.execute("SELECT user_id FROM users")
            user_ids = [row[0] for row in rows]

            return user_ids
        
        except Exception as e:
            logger.error(f'Ошибка при получении всех user_id: {e}')
            return []
        
    def get_user_by_id(self, user_id):
        try:
            result = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            result = result.fetchone()

            return result
        
        except Exception as e:
            logger.error(f'Ошибка в get_user_by_id: {e}')
            return []
        
    def update_by_id(self, user_id, value, colum):
        try:
            self.cursor.execute(f"UPDATE users SET {colum} = ? WHERE user_id = ?", (value, user_id))
            self.connection.commit()
        except Exception as e:
            logger.error(f'Ошибка в update_by_id: {e}')
            return
    

    def __del__(self):
        self.cursor.close()
        self.connection.close()

db = Database(DATABASE_NAME)