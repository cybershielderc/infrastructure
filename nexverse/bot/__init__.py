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
from .image_generation_options import (
    size_options,
    inference_steps,
    numberof_samples
)
from .image_models_menu import ai_models_image_menu
from .start_menu import start_menu_markup
from ..modelslab_api import TextToImageAsynchronous


def get_file_byte_data_from_url(file_url):
    try:
        response = requests.get(file_url)
        # Check if the request was successful
        if response.status_code == 200:
            return response.content  # Return the byte data
        else:
            print(f"Failed to retrieve file from URL: {file_url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while retrieving file from URL: {file_url}. Error: {str(e)}")
        return None


class NexVerse:
    def __init__(self, token: str, ai_image_api: TextToImageAsynchronous, lang_dict: dict):
        self.token = token
        self.ai_image_api = ai_image_api
        self.lang = lang_dict
        self.app = self._initialize_bot()

    def _initialize_bot(self) -> ApplicationBuilder:
        app: ApplicationBuilder = ApplicationBuilder().token(self.token).build()
        app.add_handler(CallbackQueryHandler(self.start_menu, "main"))
        app.add_handler(CallbackQueryHandler(self.image_ai_menu, "m1"))
        app.add_handler(CallbackQueryHandler(self.button_input))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.text_input))
        app.add_handler(CommandHandler("start", self.start_menu))
        return app

    def download_and_store(self, user_id, urls):
        if isinstance(urls, str):
            urls = [urls]  # Convert single URL string to a list

        for url in urls:
            # Extract filename from the URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            # Define the directory path
            directory = f"nexverse/ai_creations/tg_{user_id}"

            # Check if directory exists, if not create it
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Define the file path
            file_path = os.path.join(directory, filename)

            # Download the file
            try:
                urlretrieve(url, file_path)
                print(f"File downloaded and stored at: {file_path}")
            except Exception as e:
                print(f"Failed to download the file from {url}: {e}")

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
        if query.data == "regenerate_data":
            await update._bot.send_message(
                text="Regenerating... ⌛ | Please be patient this will only take a few seconds!",
                chat_id=query.message.chat_id)

            await self.reply_with_generated_image(update, context)
        if query.data.startswith('ai>img>model>selection#//'):
            selection = query.data.split("ai>img>model>selection#//")[1].split("#CNAME#")
            if update.message is None:
                await update.callback_query.edit_message_text(
                    text=self.lang['select_samples'].format(mnam=selection[1], warn="⚠️"),
                    parse_mode="HTML",
                    reply_markup=numberof_samples()
                )
            else:
                await update.callback_query.edit_message_text(
                    text=self.lang['select_samples'].format(mnam=selection[1], warn="⚠️"),
                    parse_mode="HTML",
                    reply_markup=numberof_samples()
                )
            context.user_data['selected_model'] = selection[0]
            context.user_data['selected_model_name'] = selection[1]
            # context.user_data['waiting_for_prompt'] = True
        if query.data.startswith('samples='):
            number_of_samples = query.data.split("samples=")[1]
            if update.message is None:
                await update.callback_query.edit_message_text(
                    text=self.lang['select_size'].format(
                        mnam=context.user_data['selected_model_name'],
                        samc=number_of_samples,
                    ),
                    parse_mode="HTML",
                    reply_markup=size_options()
                )
            else:
                await update.callback_query.edit_message_text(
                    text=self.lang['select_size'].format(
                        mnam=context.user_data['selected_model_name'],
                        samc=number_of_samples,
                    ),
                    parse_mode="HTML",
                    reply_markup=size_options()
                )
            context.user_data['number_of_samples'] = int(number_of_samples)
        if query.data.startswith('size='):
            image_size = query.data.split("size=")[1]
            context.user_data['image_width'] = int(image_size.split("x")[0])
            context.user_data['image_height'] = int(image_size.split("x")[1])
            if update.message is None:
                await update.callback_query.edit_message_text(
                    text=self.lang['select_inference'].format(
                        warn="⚠️",
                        mnam=context.user_data['selected_model_name'],
                        samc=context.user_data['number_of_samples'],
                        imsi=image_size.split("x")[0] + "x" + image_size.split("x")[1]
                    ),
                    parse_mode="HTML",
                    reply_markup=inference_steps()
                )
            else:
                await update.callback_query.edit_message_text(
                    text=self.lang['select_inference'].format(
                        mnam=context.user_data['selected_model_name'],
                        samc=context.user_data['number_of_samples'],
                        imsi=image_size.split("x")[0] + "x" + image_size.split("x")[1]
                    ),
                    parse_mode="HTML",
                    reply_markup=inference_steps()
                )
        if query.data.startswith('infs='):
            inference_steps_num = query.data.split("infs=")[1]
            if update.message is None:
                await update.callback_query.message.delete()
                await update.callback_query.message.reply_text(
                    text=self.lang['reply_pos_prompt'].format(
                        mnam=context.user_data['selected_model_name'],
                        samc=context.user_data['number_of_samples'],
                        imsi=f"{context.user_data['image_height']}x{context.user_data['image_width']}",
                        infs=str(inference_steps_num)
                    ),
                    parse_mode="HTML",
                    reply_markup=telegram.ForceReply()
                )
            else:
                await update.message.delete()
                await update.message.reply_text(
                    text=self.lang['reply_pos_prompt'].format(
                        mnam=context.user_data['selected_model_name'],
                        samc=context.user_data['number_of_samples'],
                        imsi=f"{context.user_data['image_height']}x{context.user_data['image_width']}",
                        infs=str(inference_steps_num)
                    ),
                    parse_mode="HTML",
                    reply_markup=telegram.ForceReply()
                )
            context.user_data['inference_steps'] = int(inference_steps_num)
            context.user_data['waiting_for_prompt'] = True

    async def reply_with_generated_image(self, update: Update, context: CallbackContext):
        try:
            image = await self.ai_image_api.handle_response(
                self.ai_image_api.get_model(context.user_data['selected_model']),
                context._user_id,
                context.user_data['pos_prompt'],
                context.user_data['neg_prompt'] if context.user_data[
                                                       'neg_prompt'] is not '-' else self.ai_image_api.DEFAULT_NEG_PROMPT,
                [context.user_data['image_width'], context.user_data['image_height']],
                context.user_data['number_of_samples'],
                context.user_data['inference_steps']
            )
        except requests.exceptions.ConnectionError:
            await update._bot.delete_message(chat_id=update.message.chat_id,
                                             message_id=context.user_data['reply_message_id'])
            await update.message.reply_text(
                text="Sorry, I couldn't generate that image for you! :/\nPlease try again!."
            )
        message = f"Successfully generated!\n<strong>Image ID</strong> <code>{image[0]}</code>\n" + \
                  f"<strong>Time Took {image[3]} seconds</strong>\n\n<strong>Prompt</strong>\n" + \
                  f"{context.user_data['pos_prompt']}\n\n<strong>Negative Prompt</strong>\n{context.user_data['neg_prompt']}" + \
                  f"\n\n<strong>Model Name</strong>\n{context.user_data['selected_model_name']}"
        if 'reply_message_id' in context.user_data:
            if context.user_data['reply_message_id'] is not None:
                await update._bot.delete_message(chat_id=update.message.chat_id,
                                                 message_id=context.user_data['reply_message_id'])
                context.user_data['reply_message_id'] = None
        if not update.message:
            if type(image[1]) is str:
                response_message = await update.callback_query.message.reply_photo(
                    photo=image[1],
                    caption=message,
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Regenerate", callback_data="regenerate_data"),
                            InlineKeyboardButton("Back to Menu", callback_data="m1")
                        ]]
                    )
                )
                context.user_data['tti_response_message'] = response_message.message_id
                self.download_and_store(context._user_id, image[1])
            elif type(image[1]) is list:
                await update.callback_query.message.reply_media_group(
                    media=[InputMediaPhoto(media=x) for x in image[1]],
                )
                response_message = await update.callback_query.message.reply_text(
                    text=message,
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Regenerate", callback_data="regenerate_data"),
                            InlineKeyboardButton("Back to Menu", callback_data="m1")
                        ]]
                    )
                )
                context.user_data['tti_response_message'] = response_message.message_id
                self.download_and_store(context._user_id, image[1])
        else:
            if type(image[1]) is str:
                response_message = await update.message.reply_photo(
                    photo=image[1],
                    caption=message,
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Regenerate", callback_data="regenerate_data"),
                            InlineKeyboardButton("Back to Menu", callback_data="m1")
                        ]]
                    )
                )
                context.user_data['tti_response_message'] = response_message.message_id
                self.download_and_store(context._user_id, image[1])
            elif type(image[1]) is list:
                await update.message.reply_media_group(
                    media=[InputMediaPhoto(media=x) for x in image[1]],
                )
                response_message = await update.message.reply_text(
                    text=message,
                    parse_mode='HTML',
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Regenerate", callback_data="regenerate_data"),
                            InlineKeyboardButton("Back to Menu", callback_data="m1")
                        ]]
                    )
                )
                context.user_data['tti_response_message'] = response_message.message_id
                self.download_and_store(context._user_id, image[1])

    async def text_input(self, update: Update, context: CallbackContext):
        if 'waiting_for_neg_prompt' in context.user_data:
            if context.user_data['waiting_for_neg_prompt']:
                if update.message.reply_to_message:
                    # Capture message
                    user_input = update.message.text
                    await update.message.delete()
                    await update.message.reply_to_message.delete()
                    await update.message.reply_text(
                        text=self.lang['final_message'].format(
                            mnam=context.user_data['selected_model_name'],
                            samc=context.user_data['number_of_samples'],
                            imsi=f"{context.user_data['image_height']}x{context.user_data['image_width']}",
                            infs=context.user_data['inference_steps'],
                            posp=context.user_data['pos_prompt'],
                            negp=user_input
                        ),
                        parse_mode="HTML",
                        reply_markup=None
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
                    await update.message.reply_to_message.delete()
                    await update.message.reply_text(
                        text=self.lang['reply_neg_prompt'].format(
                            mnam=context.user_data['selected_model_name'],
                            samc=context.user_data['number_of_samples'],
                            imsi=f"{context.user_data['image_height']}x{context.user_data['image_width']}",
                            infs=context.user_data['inference_steps'],
                            uinp=user_input,
                        ),
                        parse_mode="HTML",
                        reply_markup=telegram.ForceReply()
                    )
                    context.user_data['waiting_for_prompt'] = False
                    context.user_data['pos_prompt'] = user_input
                    context.user_data['waiting_for_neg_prompt'] = True

    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str, image_api: TextToImageAsynchronous, lang_dict: dict) -> ApplicationBuilder:
    bot = NexVerse(token, image_api, lang_dict)
    bot.run()
