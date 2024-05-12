import mysql.connector
import os


class FirstRun:
    def __init__(self, data, credentials):
        self.connection = None
        self.data = data
        self.credentials = credentials

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.data['host'],
                user=self.credentials['username'],
                password=self.credentials['password']
            )
        except mysql.connector.errors.DatabaseError as e:
            raise e
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute("SHOW DATABASES;")
            for database in self.cursor:
                print(database)
        except Exception as e:
            raise e

    def execute_scripts(self):
        files = [f for f in os.listdir() if os.path.isfile("")]
