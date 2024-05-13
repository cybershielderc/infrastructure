import mysql.connector
import os


class CheckDeveloperStatus:
    @staticmethod
    def check_developer_status(data: dict = None, credentials: dict = None, telegram_id: str = None) -> bool:
        if data is None:
            raise Exception('C')
        if telegram_id is None:
            raise Exception('Telegram ID is required')
