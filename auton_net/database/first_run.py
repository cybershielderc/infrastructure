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
            

    def execute_scripts(self):
        pass
