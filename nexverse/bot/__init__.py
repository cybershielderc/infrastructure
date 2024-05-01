import asyncio

import requests.exceptions
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
from ..modelslab_api import MODEL, TextToImage

import re
import time


class NexVerse:
    def __init__(self, token: str, ai_image_api: TextToImage):
        self.token = token
        self.ai_image_api = ai_image_api
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
            context.user_data['selected_model_name'] = selection[1]
            context.user_data['waiting_for_prompt'] = True

    async def reply_with_generated_image(self, update: Update, context: CallbackContext):
        try:
            image = self.ai_image_api.build_request(
                self.ai_image_api.get_model(context.user_data['selected_model']),
                context.user_data['pos_prompt'],
                context.user_data['neg_prompt'] if context.user_data[
                                                       'neg_prompt'] is not '-' else self.ai_image_api.DEFAULT_NEG_PROMPT
            ).json()
        except requests.exceptions.ConnectionError:
            await update._bot.delete_message(chat_id=update.message.chat_id,
                                             message_id=context.user_data['reply_message_id'])
            await update.message.reply_text(
                text="Sorry, I couldn't generate that image for you! :/\nPlease try again!."
            )
        print(image)
        print(self.ai_image_api.get_model(context.user_data['selected_model']))
        print(context.user_data['pos_prompt'])
        message = f"Successfully generated!\n<strong>Image ID</strong> <code>{image['id']}</code>\n" + \
                  f"<strong>Time Took {image['generationTime']:.2f} seconds</strong>\n\n<strong>Prompt</strong>\n" + \
                  f"{context.user_data['pos_prompt']}\n\n<strong>Negative Prompt</strong>\n{context.user_data['neg_prompt']}" + \
                  f"\n\n<strong>Model Name</strong>\n{context.user_data['selected_model_name']}"
        await update._bot.delete_message(chat_id=update.message.chat_id,
                                         message_id=context.user_data['reply_message_id'])
        await update.message.reply_photo(
            photo=image['output'][0],
            caption=message,
            parse_mode='HTML'
        )

    async def text_input(self, update: Update, context: CallbackContext):
        if 'waiting_for_neg_prompt' in context.user_data:
            if context.user_data['waiting_for_neg_prompt']:
                if update.message.reply_to_message:
                    # Capture message
                    user_input = update.message.text
                    await update.message.delete()
                    await update.message.reply_to_message.edit_text(
                        text=f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n<strong>User Prompt</strong>\n" +
                             context.user_data[
                                 'pos_prompt'] + "\n\n<strong>User Negative Prompt</strong>\n" + user_input,
                        parse_mode="HTML",
                        reply_markup=ai_models_image_menu()
                    )
                    processing_message = await update.message.reply_text(
                        "Processing... ⌛ | Please be patient this will only take a few seconds!"
                    )
                    context.user_data['neg_prompt'] = user_input
                    context.user_data['reply_message_id'] = processing_message.message_id
                    context.user_data['waiting_for_neg_prompt'] = False
                    await self.reply_with_generated_image(update, context)
        if 'waiting_for_prompt' in context.user_data:
            if context.user_data['waiting_for_prompt']:
                if update.message.reply_to_message:
                    # Capture message
                    user_input = update.message.text
                    await update.message.delete()
                    await update.message.reply_to_message.edit_text(
                        text=f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n<strong>User Prompt</strong>\n" + user_input + "\n\n<strong>\nPlease reply to this message once more to set the negative prompt you would like the AI to use!</strong>\n<strong>Or reply with - to use the default negative prompt</strong>",
                        parse_mode="HTML",
                        reply_markup=ai_models_image_menu()
                    )
                    context.user_data['waiting_for_prompt'] = False
                    context.user_data['pos_prompt'] = user_input
                    context.user_data['waiting_for_neg_prompt'] = True

    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str, image_api: TextToImage) -> ApplicationBuilder:
    bot = NexVerse(token, image_api)
    bot.run()
