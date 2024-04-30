import asyncio
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    ContextTypes,
    filters
)

import re
import time


class NexVerse:
    def __init__(self, token: str):
        self.token = token
        self.app = self._initialize_bot()
    def 