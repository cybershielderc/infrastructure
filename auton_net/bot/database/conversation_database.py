import mysql.connector
import os
import uuid


class RetrieveAllConversations:
    @staticmethod
    def get_all_conversations(cls, data: dict = None):
        if not data: raise Exception("No database datat provided")
        query = f'''SELECT conversation.initiator_id, conversation.participant_id WHERE conversation.isHolding = 1 '''
