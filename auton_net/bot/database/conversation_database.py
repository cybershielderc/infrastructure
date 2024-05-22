import mysql.connector
import os
import uuid


class RetrieveAllConversations:
    @staticmethod
    def get_all_conversations(data: dict = None):
        """
        Retrieves all holding conversations that are currently holding and are not paused
        returns a list of tuples that store the initiator of the conversation and participant of the conversation
        """
        if not data: raise Exception("No database datat provided")
        query = f'''SELECT initiator_id, participant_id FROM conversation WHERE isHolding = 1;'''
        try:
            connection = mysql.connector.connect(
                host=data['host'],
                port=3306,
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
