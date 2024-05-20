import mysql.connector
import os
import uuid

class RetrieveAllConversations:
    @staticmethod
    def get_all_conversations(cls, data: dict = None):
        if not data: 