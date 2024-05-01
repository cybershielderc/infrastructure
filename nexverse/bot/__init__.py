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
from .image_models_menu import ai_models_image_menu

import re
import time


class NexVerse:
    def __init__(self, token: str):
        self.token = token
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> ApplicationBuilder:
        app: ApplicationBuilder = ApplicationBuilder().token(self.token).build()
        app.add_handler(CallbackQueryHandler(self.start_menu, "main"))
        app.add_handler(CallbackQueryHandler(self.image_ai_menu, "m1"))
        app.add_handler(CallbackQueryHandler(self.button_input))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.text_input))
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
            )

    async def image_ai_menu(self, update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text="Please select a model to generate the image with!",
            reply_markup=ai_models_image_menu()
        )

    async def button_input(self, update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        if query.data.startswith('ai>img>model>selection#//'):
            selection = query.data.split("ai>img>model>selection#//")[1].split("#CNAME#")
            if update.message is None:
                await update.callback_query.edit_message_text(
                    text=f"You have selected <strong>{selection[1]}</strong>\nPlease reply to this message to set the prompt you would like the AI to use!",
                    parse_mode="HTML",
                    reply_markup=ai_models_image_menu()
                )
            else:
                await update.message.edit_caption(
                    caption=f"You have selected <strong>{selection[1]}</strong>\nPlease reply to this message to set the prompt you would like the AI to use!",
                    parse_mode="HTML",
                    reply_markup=ai_models_image_menu())
            context.user_data['selected_model'] = selection[0]
            context.user_data['waiting_for_prompt'] = True

    async def text_input(self, update: Update, context: CallbackContext):
        if 'waiting_for_prompt' in context.user_data:
            if context.user_data['waiting_for_prompt']:
                if update.message.reply_to_message:
                    # Capture message
                    user_input = update.message.text
                    await update.message.delete()
                    await update.message.reply_text(f'You entered: {user_input}')
                    context.user_data['waiting_for_prompt'] = False

    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str) -> ApplicationBuilder:
    bot = NexVerse(token)
    bot.run()
