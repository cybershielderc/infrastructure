import mysql.connector
import os


class CheckDeveloperStatus:
    @staticmethod
    def check_developer_status(data: dict, credentials: dict, telegram_id: str = None) -> bool:
        if telegram_id is None:
            raise Exception('Telegram ID is required')
