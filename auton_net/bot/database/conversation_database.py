import mysql.connector
import os
import uuid


class RetrieveAllConversations:
    @staticmethod
    def get_all_conversations(cls, data: dict = None):
        if not data: raise Exception("No database datat provided")
        query = f'''SELECT conversation.initiator_id, conversation.participant_id WHERE conversation.isHolding = 1;'''
        try:
            connection = mysql.connector.connect(
                host=data['host'],
                user=data['username'],
                password=data['password'],
                database=data['database']
            )
        except mysql.connector.errors.DatabaseError as e:
            raise e
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            _u = cursor.fetchall()
            cursor.close()
            connection.close()
            return _u
        except Exception as e:
            raise e
