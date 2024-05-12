import mysql.connector


class FirstRun:
    def __init__(self, data, credentials):
        self.connection = None
        self.data = data
        self.credentials = credentials

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.data['host'] + ':' + self.data['port'],
            user=self.credentials['username'],
            password=self.credentials['password']
        )
