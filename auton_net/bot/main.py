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
from .menus import (
    start_menu,
    marketplace_panel
)


class AutonNET:
    def __init__(self, token: str, lang_dict: dict = {}):
        self.token = token
        self.lang = lang_dict
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> ApplicationBuilder:
        app: ApplicationBuilder = ApplicationBuilder().token(self.token).build()
        app.add_handler(CallbackQueryHandler(self.mp_panel, "mp_1"))
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
                reply_markup=start_menu() if not menu else menu,
            )
        else:
            await update.message.reply_text(
                text=caption,
                parse_mode='HTML',
                reply_markup=start_menu() if not menu else menu,
            )

    async def image_ai_menu(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text=query.,
            reply_markup=marketplace_panel()
        )

    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str, lang_dict: dict) -> ApplicationBuilder:
    bot = AutonNET(token, lang_dict)
    bot.run()
