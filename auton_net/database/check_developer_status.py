import mysql.connector
import os


class CheckDeveloperStatus:
    @staticmethod
    def check_developer_status(data: dict = None, credentials: dict = None, telegram_id: str = None) -> bool:
        if data is None:
            raise Exception('data is required')
        if credentials is None:
            raise Exception('credentials are required')
        if telegram_id is None:
            raise Exception('Telegram ID is required')
        try:
            connection = mysql.connector.connect(
                host=data['host'],
                user=credentials['username'],
                password=credentials['password'],
                database=data['database']
            )
        except mysql.connector.errors.DatabaseError as e:
            raise e
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM developers WHERE tg_id = {telegram_id}")
            for database in cursor:
                print(database)
        except Exception as e:
            raise e
