import mysql.connector


class FirstRun:
    def __init__(self, data, credentials):
        self.data = data
        self.credentials = credentials

    def connect(self):
        mydb = mysql.connector.connect(
            host=self.data['host'],
            user="yourusername",
            password="yourpassword"
        )
