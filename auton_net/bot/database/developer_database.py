from datetime import date, datetime, timedelta, time
from typing import Any, List, Set

import mysql.connector
import os
import uuid

from _decimal import Decimal


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
    def create_developer(
            host: str = None,
            database: str = None,
            username: str = None,
            password: str = None,
            telegram_id: int = None,
            accepted_budget_min: int = 0,
            accepted_budget_max: int = 0,
            accepted_worktime_min: int = 0,
            accepted_worktime_max: int = 0,
            isAnonymous: int = 0,
            nickname: str = "Anonymous Developer",
            wallet_address: str = "0xdead",
    ) -> bool:
        print(f"Telegram ID is {telegram_id} and is {len(str(telegram_id))} numbers long")
        if password is None or username is None or database is None or host is None:
            raise Exception('data is required')
        if telegram_id is None:
            raise Exception('Telegram ID is required')
        try:
            connection = mysql.connector.connect(
                host=host.split(":")[0],
                port=host.split(":")[1],
                user=username,
                password=password,
                database=database
            )
        except mysql.connector.errors.DatabaseError as e:
            raise e
        try:
            cursor = connection.cursor()
            statement = f"""
            INSERT INTO `developers`
            (`tg_id`,`developer_uuid`, `linked_portfolio_rid`, `accepted_budget_min`, `accepted_budget_max`, `accepted_worktime_min`, `accepted_worktime_max`, `rating`, `isVerified`, `isAnonymous`, `nickname`, `connected_wallet`, `completed_orders`, `open_orders`, `rejected_orders`, `avg_completion_time`, `isAddressVerified`)
            VALUES
            (
            {telegram_id},
            '{str(uuid.uuid4())}',
            -1, 
            {accepted_budget_min}, 
            {accepted_budget_max}, 
            {accepted_worktime_min},
            {accepted_worktime_max}, 
            5.0, 
            0, 
            {isAnonymous}, 
            '{nickname}', 
            '{wallet_address}', 
            0, 
            0, 
            0, 
            0.0, 
            0);
            """
            cursor.execute(statement)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            raise e


class GetDeveloperInformation:
    @staticmethod
    def get_developer_information(
            host: str = None, database: str = None, username: str = None, password: str = None, telegram_id: int = None
    ) -> list[bool | list[
        Decimal | bytes | date | datetime | float | int | set[str] | str | timedelta | None | time | Any]] | list[
             Exception] | list[list[Any] | None]:
        """
        Gets developer information and returns it as a list object formatting in such a way
        @return [
            accepted_budget_min, integer
            accepted_budget_max, integer
            accepted_worktime_min, integer
            accepted_worktime_max, integer
            rating, float between 1-5
            isVerified, boolean
            isAnonymous, boolean
            nickname, string
            completed_orders, integer
            open_orders, integer
            rejected_orders, integer
            avg_completion_time, float
            isAddressVerified, boolean
            connected_wallet, boolean
            developer_uuid, string
        ]
        """
        if password is None or username is None or database is None or host is None:
            raise Exception('data is required')
        if telegram_id is None:
            raise Exception('Telegram ID is required')
        try:
            connection = mysql.connector.connect(
                host=host.split(":")[0],
                port=host.split(":")[1],
                user=username,
                password=password,
                database=database
            )
        except mysql.connector.errors.DatabaseError as e:
            raise e
        try:
            cursor = connection.cursor()
            cursor.execute(
                f"""SELECT * FROM developers WHERE tg_id={telegram_id};"""
            )
            result = cursor.fetchone()
            if result is None or len(result) == 0:
                cursor.close()
                connection.close()
                raise Exception(
                    f"Fatal SQL Error occurred when trying to fetch Seller information! for U-{telegram_id}")
            return [True, [
                result[3],  # accepted_budget_min
                result[4],  # accepted_budget_max
                result[5],  # accepted_worktime_min
                result[6],  # accepted_worktime_max
                result[7],  # rating
                True if result[8] == 1 else False,  # isVerified
                True if result[9] == 1 else False,  # isAnonymous
                result[10],  # nickname
                result[12],  # completed_orders
                result[13],  # open_orders
                result[14],  # rejected orders
                result[15],  # average completion time
                True if result[16] == 1 else False,  # Is Address Verified,
                result[1],  # Developer UUID
            ]]
        except Exception as e:
            return [e, []]
