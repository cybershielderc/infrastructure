import mysql.connector
from typing import Any

class CreateConversation:
    @staticmethod
    def create(data: dict = None, initiator_id: int = None, participant_id: int = None, isHolding: bool = False) -> bool:
        if not data:
            raise Exception("No database datat provided")
        query = f'''
            INSERT INTO conversation (initiator_id, participant_id, nomfi, nomfp, conversation_initiated, isHolding, agreed_price)
            VALUES ({initiator_id}, {participant_id}, 0, 0, UNIX_TIMESTAMP(), 1, 0.0);'''
        try:
            connection = mysql.connector.connect(
                host=data['host'].split(":")[0],
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
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Exception as e:
            raise e

class RetrieveConversations:
    @staticmethod
    def get_all_conversations(data: dict = None) -> list[tuple[int,int]]:
        """
        Retrieves all holding conversations that are currently holding and are not paused
        returns a list of tuples that store the initiator of the conversation and participant of the conversation
        """
        if not data:
            raise Exception("No database datat provided")
        query = '''SELECT initiator_id, participant_id FROM conversation WHERE isHolding = 1;'''
        try:
            connection = mysql.connector.connect(
                host=data['host'].split(":")[0],
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
    @staticmethod
    def get_conversation(data: dict = None, searchee_id: int = None) -> tuple[Any]:
        """
        Retrieves a conversation by its participant or initiator ID
        """
        if not data:
            raise Exception("No database datat provided")
        query = f'''
                SELECT *
                FROM conversations
                WHERE (initiator_id = '{searchee_id}' or participant_id = '{searchee_id}');'''
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
