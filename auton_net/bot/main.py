import datetime
import json
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    filters,
    CallbackQueryHandler, Application
)

from .actions.register.developer.register_logic import register_logic as seller_register_logic
from .actions.register.developer.register_text_input import handle_seller_text_input as seller_register_text
from .database import (
    CheckDeveloperStatus
)
from .menus import (
    start_menu,
    marketplace_panel,
    developer_panel_main,
    developer_panel_register,
    developer_panel_is_anonymous
)
from .database import (
    FirstRun,
    CheckDeveloperStatus,
D
)


def ftime() -> str:
    return datetime.datetime.now().strftime("%d-%m-%Y//%H:%M:%S.%f")


def fprint(system, string, end='\n'):
    out_string = f"[{ftime()}]({system}): {string}"
    print(out_string, end=end)


class AutonNET:
    def __init__(self, token: str, bot_data: dict = {}, lang_dict: dict = {}):
        self.token = token
        self.lang = lang_dict
        self.bot_data = bot_data
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> Application:
        app: Application = ApplicationBuilder().token(self.token).build()
        app.bot_data["database_host"] = f"{self.bot_data['database']['host']}:{self.bot_data['database']['port']}"
        app.bot_data["database_user"] = f"{self.bot_data['database']['credentials']['username']}"
        app.bot_data["database_password"] = f"{self.bot_data['database']['credentials']['password']}"
        app.bot_data["database_database"] = f"{self.bot_data['database']['database']}"
        app.bot_data["developer_panel"] = developer_panel_main
        app.add_handler(CallbackQueryHandler(self.mp_panel, "mp_1"))
        app.add_handler(CallbackQueryHandler(self.mp_dev_register_1, "mp_dev_start_registration"))
        app.add_handler(CallbackQueryHandler(self.mp_dev_panel, "mp_dev"))
        # app.add_handler(CallbackQueryHandler(self.mp_dev_register_1, "mp_dev_start_registration"))
        # app.add_handler(CallbackQueryHandler(self.start_menu, "main"))
        # app.add_handler(CallbackQueryHandler(self.image_ai_menu, "m1"))
        app.add_handler(CallbackQueryHandler(self.registeration_input))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.text_input))
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

    async def mp_dev_register_1(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        await query.answer()
        context.user_data['devRegistration'] = True
        fprint("REGS", f"devRegistration is now enabled for U-{update.effective_user.id}")
        await query.edit_message_caption(
            caption="Would you like to remain anonymous on our platform?\n" + \
                    "By selecting <strong>yes</strong> your name will be kept hidden\n" + \
                    "when communicating with a client!, Instead a nickname will be shown!\n" + \
                    "By selecting <strong>no</strong> your name will be visible by the\n" + \
                    "receiving end!",
            parse_mode='HTML',
            reply_markup=developer_panel_is_anonymous(),
        )

    async def mp_dev_panel(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        await query.answer()
        # Check if user is a developer
        if CheckDeveloperStatus.check_developer_status(
                self.bot_data['database'], self.bot_data['database']['credentials'],
                str(update.effective_user.id)
        ):
            await query.edit_message_reply_markup(reply_markup=developer_panel_main())
        else:
            await query.edit_message_caption(
                caption="Sorry, but you have not been registered as a developer!\nWould you like to register?",
                reply_markup=developer_panel_register()
            )

    async def mp_dev_panel_stats(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        await query.answer()
        # Check if user is a developer
        seller_stats =
            await query.edit_message_reply_markup(reply_markup=developer_panel_main())
        else:
            await query.edit_message_caption(
                caption="Sorry, but you have not been registered as a developer!\nWould you like to register?",
                reply_markup=developer_panel_register()
            )

    async def registeration_input(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        if query.data.startswith("ignore_0xdead"): await query.answer()
        if 'devRegistration' in context.user_data:
            await seller_register_logic(update, context)
        if 'clientRegistration' in context.user_data:
            await seller_register_logic(update, context)
        await query.answer()

    async def text_input(self, update: Update, context: CallbackContext):
        if 'devRegistration' in context.user_data:
            await seller_register_text(update, context)

    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str, bot_data: dict, lang_dict: dict) -> ApplicationBuilder:
    bot = AutonNET(token, bot_data, lang_dict)
    bot.run()
