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
    marketplace_panel,
    developer_panel_main
)
from .database import (
    CheckDeveloperStatus
)


class AutonNET:
    def __init__(self, token: str, bot_data: dict = {}, lang_dict: dict = {}):
        self.token = token
        self.lang = lang_dict
        self.bot_data = bot_data
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> ApplicationBuilder:
        app: ApplicationBuilder = ApplicationBuilder().token(self.token).build()
        app.add_handler(CallbackQueryHandler(self.mp_panel, "mp_1"))
        app.add_handler(CallbackQueryHandler(self.mp_dev_panel, "mp_dev"))
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
            await update.callback_query.message.reply_photo(
                caption=caption,
                parse_mode='HTML',
                reply_markup=start_menu() if not menu else menu,
                photo=open("./bot/images/banners/banner.jpg", "rb"),
            )
        else:
            await update.message.reply_photo(
                caption=caption,
                parse_mode='HTML',
                reply_markup=start_menu() if not menu else menu,
                photo=open("./bot/images/banners/banner.jpg", "rb"),
            )

    async def mp_panel(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        await query.answer()
        await query.edit_message_reply_markup(
            reply_markup=marketplace_panel(),
        )

    async def mp_dev_panel(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        await query.answer()
        # Check if user is a developer
        if CheckDeveloperStatus.check_developer_status(
                self.bot_data['database'], self.bot_data['database']['credentials'],
                str(update.effective_user.id)
        ):
            await query.edit_message_reply_markup(
                reply_markup=developer_panel_main()
            )
        else:
            await query.edit_message_text(
                text="Sorry, but you have not been registered as a developer!\nWould you like to register?",
                reply_markup=None
            )

    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str, bot_data: dict, lang_dict: dict) -> ApplicationBuilder:
    bot = AutonNET(token, bot_data, lang_dict)
    bot.run()
