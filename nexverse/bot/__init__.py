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
from .start_menu import start_menu_markup

import re
import time


class NexVerse:
    def __init__(self, token: str):
        self.token = token
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> ApplicationBuilder:
        app: ApplicationBuilder = ApplicationBuilder().token(self.token).build()
        # app.add_handler(CallbackQueryHandler(self.button_handler))
        # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.text_input))
        app.add_handler(CommandHandler("start", self.start_menu))
        return app

    async def m(self, update: Update, context: CallbackContext, message: str = None) -> None:
        caption = f'<strong>{message}</strong>' if message else \
            f'<strong>Hi {update.effective_user.name}</strong>'
        if update.message is None:
            await update.callback_query.message.reply_text(
                text=caption,
                parse_mode='HTML',
                reply_markup=start_menu_markup(),
            )
        else:
            await update.message.reply_text(
                text=caption,
                parse_mode='HTML',
                reply_markup=start_menu_markup(),
            )

    async def image_to_image(self, update: Update, context: CallbackContext) -> None:


    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str) -> ApplicationBuilder:
    bot = NexVerse(token)
    bot.run()
