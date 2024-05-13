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
            _u = cursor.fetchone()
            cursor.close()
            connection.close()
            return True if _u else False
        except Exception as e:
            raise e


class CreateDeveloperDatapoint:
    @staticmethod
    def create_developer(data: dict = None,
                         credentials: dict = None,
                         telegram_id: str = None,
                         accepted_budget_min: int = None,
                         accepted_budget_max: int = None,
                         accepted_worktime_min: int = None,
                         accepted_worktime_max: int = None,
                         isAnonymous: int = None,
                         
                         ) -> bool:
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
            statement = f"""
            INSERT INTO `developers`
            (`tg_id`, `linked_portfolio_rid`, `accepted_budget_min`, `accepted_budget_max`, `accepted_worktime_min`, `accepted_worktime_max`, `rating`, `isVerified`, `isAnonymous`, `nickname`, `connected_wallet`, `completed_orders`, `open_orders`, `rejected_orders`, `avg_completion_time`, `isAddressVerified`)
            VALUES
            ({telegram_id}, -1, {accepted_budget_min}, {accepted_budget_max}, {accepted_worktime_min},{accepted_worktime_max}, 5.0, 0, {isAnonymous}, 'Anonymous Developer', '0xdead', 0, 0, 0, 1.5, 0);
            """
        except Exception as e:
            raise e
