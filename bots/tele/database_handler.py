import mysql.connector, json
from mysql.connector import DatabaseError, Error
from os.path import isfile, join
from os import listdir

class DatabaseHandler:
    __slots__ = ("_connection", "_cursor", "_host", "_username", "_password", "_database")

    def __init__(self):
        self._cursor = None
        self._connection = None
        with open("/cfgs/bots.json", "r") as data:
            jdata = json.loads(data.read())
            self._host = jdata['database']['host']
            self._username = jdata['database']['user']
            self._password = jdata['database']['password']
            self._database = jdata['database']['database']
            data.close()

    def connect(self) -> True | False:
        try:
            self._connection = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database=self._database
            )
            return self._connection.is_connected()
        except DatabaseError:
            return False

    def disconnect(self) -> True | False:
        try:
            self._connection.close()
            return self._connection.is_connected()
        except DatabaseError:
            return False

    def initiate_cursor(self) -> True | False:
        try:
            self._cursor : mysql.connector.MySQLConnection = self._connection.cursor()
            return self._cursor.is_connected()
        except DatabaseError as e:
            return False

    def executeQueries(self) -> list[True | False]:
        QUERY_FOLDER = "/bots/tele/sql_queries/"
        files = [
            join(QUERY_FOLDER, file) for file in listdir(
                join(QUERY_FOLDER)
            ) if isfile(
                join(QUERY_FOLDER, file)
            ) and file.endswith(".sql")
        ]

