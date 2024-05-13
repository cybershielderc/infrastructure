import mysql.connector
import os


class CheckDeveloperStatus:
    @staticmethod
    def check_developer_status(data: dict, credentials: dict, telegram_id: str = None) -> bool:
        