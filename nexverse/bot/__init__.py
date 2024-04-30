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
    filters,
    CallbackQueryHandler
)

import re
import time


class NexVerse:
    def __init__(self, token: str):
        self.token = token
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> ApplicationBuilder:
        app: ApplicationBuilder = ApplicationBuilder().token(self.token).build()
        app.add_handler(CallbackQueryHandler(self.button_handler))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND))
