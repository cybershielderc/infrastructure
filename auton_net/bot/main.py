import requests.exceptions
import telegram
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    InputMediaPhoto
)
from telegram.constants import ParseMode
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    filters,
    CallbackQueryHandler, Application
)
import os
from urllib.request import urlretrieve
from urllib.parse import urlparse
from .menus import (
    start_menu,
    marketplace_panel,
    developer_panel_main,
    developer_panel_register,
    developer_panel_is_anonymous
)
from .database import (
    CheckDeveloperStatus,
    CreateDeveloperDatapoint
)
from ..bot.actions.register.developer import register_logic as seller_register_logic
import datetime


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
            await query.edit_message_reply_markup(
                reply_markup=developer_panel_main()
            )
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
            if 'dev_reg#anon#nickname#awaiting' in context.user_data:
                if context.user_data['dev_reg#anon#nickname#awaiting']:
                    if update.message.reply_to_message:
                        # Capture message
                        user_input = update.message.text
                        await update.message.delete()
                        await update.message.reply_to_message.delete()
                        fprint("RTXI", f"U-{update.effective_user.id} gave {user_input} as a nickname")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                        context.user_data['dev_reg#anon#nickname#awaiting'] = False
                        context.user_data['dev_reg#var><nickname'] = user_input
                        fprint("RTXI", f"U-{update.effective_user.id}>> Saved Nickname to user data until confirmation")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                        await update.message.reply_text(
                            text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                                 f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                                 f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                                 f'\nAre you sure this is the nickname you want?',
                            parse_mode='HTML',
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton('✅ Yes', callback_data='dev_reg#nick#confirmation>>yes'),
                                        InlineKeyboardButton('❌ No', callback_data='dev_reg#nick#confirmation>>no')
                                    ]
                                ]
                            )
                        )
            if 'dev_reg#budget#min#awaiting' in context.user_data:
                if context.user_data['dev_reg#budget#min#awaiting']:
                    if update.message.reply_to_message:
                        # Capture message
                        user_input = update.message.text
                        await update.message.delete()
                        await update.message.reply_to_message.delete()
                        fprint("RTXI", f"U-{update.effective_user.id} gave {user_input}$ as a min budget")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                        context.user_data['dev_reg#budget#min#awaiting'] = False
                        context.user_data['dev_reg#var><min_budget'] = user_input
                        fprint("RTXI",
                               f"U-{update.effective_user.id}>> Saved Min Budget to user data until confirmation")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                        await update.message.reply_text(
                            text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                                 f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                                 f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                                 f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                                 f'\nAre you sure this is the minimum accepted price you want?',
                            parse_mode='HTML',
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton('✅ Yes',
                                                             callback_data='dev_reg#min_budget#confirmation>>yes'),
                                        InlineKeyboardButton('❌ No',
                                                             callback_data='dev_reg#min_budget#confirmation>>no')
                                    ]
                                ]
                            )
                        )
            if 'dev_reg#budget#max#awaiting' in context.user_data:
                if context.user_data['dev_reg#budget#max#awaiting']:
                    if update.message.reply_to_message:
                        # Capture message
                        user_input = update.message.text
                        await update.message.delete()
                        await update.message.reply_to_message.delete()
                        fprint("RTXI", f"U-{update.effective_user.id} gave {user_input}$ as a max budget")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                        context.user_data['dev_reg#budget#max#awaiting'] = False
                        context.user_data['dev_reg#var><max_budget'] = user_input
                        fprint("RTXI",
                               f"U-{update.effective_user.id}>> Saved Min Budget to user data until confirmation")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                        await update.message.reply_text(
                            text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                                 f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                                 f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                                 f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                                 f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                                 f'\nAre you sure this is the maximum accepted price you want?',
                            parse_mode='HTML',
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton('✅ Yes',
                                                             callback_data='dev_reg#max_budget#confirmation>>yes'),
                                        InlineKeyboardButton('❌ No',
                                                             callback_data='dev_reg#max_budget#confirmation>>no')
                                    ]
                                ]
                            )
                        )
            if 'dev_reg#timeframe#min#awaiting' in context.user_data:
                if context.user_data['dev_reg#timeframe#min#awaiting']:
                    if update.message.reply_to_message:
                        # Capture message
                        user_input = update.message.text
                        await update.message.delete()
                        await update.message.reply_to_message.delete()
                        fprint("RTXI", f"U-{update.effective_user.id} gave {user_input} as a min timeframe")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                        context.user_data['dev_reg#timeframe#min#awaiting'] = False
                        context.user_data['dev_reg#var><min_timeframe'] = user_input
                        fprint("RTXI",
                               f"U-{update.effective_user.id}>> Saved Min Timeframe to user data until confirmation")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                        await update.message.reply_text(
                            text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                                 f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                                 f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                                 f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                                 f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                                 f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
 \
                                 f'\nAre you sure this is the minimum accepted timeframe you want?',
                            parse_mode='HTML',
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton('✅ Yes',
                                                             callback_data='dev_reg#min_timeframe#confirmation>>yes'),
                                        InlineKeyboardButton('❌ No',
                                                             callback_data='dev_reg#min_timeframe#confirmation>>no')
                                    ]
                                ]
                            )
                        )
            if 'dev_reg#timeframe#max#awaiting' in context.user_data:
                if context.user_data['dev_reg#timeframe#max#awaiting']:
                    if update.message.reply_to_message:
                        # Capture message
                        user_input = update.message.text
                        await update.message.delete()
                        await update.message.reply_to_message.delete()
                        fprint("RTXI", f"U-{update.effective_user.id} gave {user_input} as a max timeframe")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                        context.user_data['dev_reg#timeframe#max#awaiting'] = False
                        context.user_data['dev_reg#var><max_timeframe'] = user_input
                        fprint("RTXI",
                               f"U-{update.effective_user.id}>> Saved Min Timeframe to user data until confirmation")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                        await update.message.reply_text(
                            text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                                 f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                                 f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                                 f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                                 f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                                 f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                                 f'<strong>Maximum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                                 f'\nAre you sure this is the maximum accepted timeframe you want?',
                            parse_mode='HTML',
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton('✅ Yes',
                                                             callback_data='dev_reg#max_timeframe#confirmation>>yes'),
                                        InlineKeyboardButton('❌ No',
                                                             callback_data='dev_reg#max_timeframe#confirmation>>no')
                                    ]
                                ]
                            )
                        )
            if 'dev_reg#wallet_addr#awaiting' in context.user_data:
                if context.user_data['dev_reg#wallet_addr#awaiting']:
                    if update.message.reply_to_message:
                        # Capture message
                        user_input = update.message.text
                        await update.message.delete()
                        await update.message.reply_to_message.delete()
                        fprint("RTXI", f"U-{update.effective_user.id} gave {user_input} as a eth wallet timeframe")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Showing confirmation menu")
                        context.user_data['dev_reg#wallet_addr#awaiting'] = False
                        context.user_data['dev_reg#var><eth_address'] = user_input
                        fprint("RTXI",
                               f"U-{update.effective_user.id}>> Saved Eth address to user data until confirmation")
                        fprint("RTXI", f"U-{update.effective_user.id}>> Set Awaiting Status to False")
                        await update.message.reply_text(
                            text=f'<strong>Registration Form</strong> <code>D-{update.effective_user.id}</code>' + \
                                 f'\n<strong>Is Anonymous?</strong> <code>{context.user_data["dev_reg#var><isAnonReadable"]}</code>\n' + \
                                 f'<strong>Nickname</strong> <code>{context.user_data["dev_reg#var><nickname"]}</code>\n' + \
                                 f'<strong>Minimum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><min_budget"]}$</code>\n' + \
                                 f'<strong>Maximum Price (In USD)</strong> <code>{context.user_data["dev_reg#var><max_budget"]}$</code>\n' + \
                                 f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><min_timeframe"]}</code>\n' + \
                                 f'<strong>Minimum Timeframe (In Days)</strong> <code>{context.user_data["dev_reg#var><max_timeframe"]}</code>\n' + \
                                 f'<strong>Ethereum Wallet Address</strong> <code>{context.user_data["dev_reg#var><eth_address"]}</code>\n' + \
                                 f'\nAre you sure this is the ethereum wallet address you want linked to your account?',
                            parse_mode='HTML',
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton('✅ Yes',
                                                             callback_data='dev_reg#wallet_addr#confirmation>>yes'),
                                        InlineKeyboardButton('❌ No',
                                                             callback_data='dev_reg#wallet_addr#confirmation>>no')
                                    ]
                                ]
                            )
                        )

    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str, bot_data: dict, lang_dict: dict) -> ApplicationBuilder:
    bot = AutonNET(token, bot_data, lang_dict)
    bot.run()
