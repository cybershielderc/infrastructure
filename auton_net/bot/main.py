import requests.exceptions
import telegram
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    InputMediaPhoto
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    filters,
    CallbackQueryHandler
)
import os
from urllib.request import urlretrieve
from urllib.parse import urlparse


def start_menu_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🛠️ Services 🧾", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Text-to-Image (TTI)", callback_data="m1"),
                # InlineKeyboardButton("Image-to-Image (WIP)", callback_data="ignore_0xdead"),  # "image_to_image"),
                # InlineKeyboardButton("AI Assistant (WIP)", callback_data="ignore_0xdead"),  # "initiate_chat"),
            ]
        ]
    )


class NexVerse:
    def __init__(self, token: str, lang_dict: dict = {}):
        self.token = token
        self.lang = lang_dict
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> ApplicationBuilder:
        app: ApplicationBuilder = ApplicationBuilder().token(self.token).build()
        # app.add_handler(CallbackQueryHandler(self.start_menu, "main"))
        # app.add_handler(CallbackQueryHandler(self.image_ai_menu, "m1"))
        # app.add_handler(CallbackQueryHandler(self.button_input))
        # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.text_input))
        app.add_handler(CommandHandler("start", self.start_menu))
        return app

    async def start_menu(self, update: Update, context: CallbackContext, message: str = None,
                         menu: InlineKeyboardMarkup = None) -> None:
        caption = f'<strong>{message}</strong>' if message else \
            f'<strong>Hi {update.effective_user.name}</strong>'
        if update.message is None:
            await update.callback_query.message.reply_text(
                text=caption,
                parse_mode='HTML',
                reply_markup=start_menu_markup() if not menu else menu,
            )
        else:
            await update.message.reply_text(
                text=caption,
                parse_mode='HTML',
                reply_markup=start_menu_markup() if not menu else menu,
           