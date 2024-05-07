import requests.exceptions
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
    def __init__(self, token: str, ai_image_api: TextToImageAsynchronous):
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
        if query.data == "regenerate_data":
            await update._bot.send_message(
                text="Regenerating... ⌛ | Please be patient this will only take a few seconds!",
                chat_id=query.message.chat_id)

            await self.reply_with_generated_image(update, context)
        if query.data.startswith('ai>img>model>selection#//'):
            selection = query.data.split("ai>img>model>selection#//")[1].split("#CNAME#")
            if update.message is None:
                await update.callback_query.edit_message_text(
                    text=f"You have selected <strong>{selection[1]}</strong>\nPlease select the amount of samples you would like the\nbot to generate!",
                    parse_mode="HTML",
                    reply_markup=numberof_samples()
                )
            else:
                await update.callback_query.edit_message_text(
                    text=f"You have selected <strong>{selection[1]}</strong>\nPlease select the amount of samples you would like the\nbot to generate!",
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
                    text=f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n<strong>Sample Count </strong><code>{number_of_samples}</code>\nPlease select the size of the image you would like the AI to use!",
                    parse_mode="HTML",
                    reply_markup=size_options()
                )
            else:
                await update.callback_query.edit_message_text(
                    text=f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n<strong>Sample Count </strong><code>{number_of_samples}</code>\nPlease select the size of the image you would like the AI to use!",
                    parse_mode="HTML",
                    reply_markup=size_options()
                )
            context.user_data['number_of_samples'] = int(number_of_samples)
        if query.data.startswith('size='):
            image_size = query.data.split("size=")[1]
            if update.message is None:
                message = \
                    f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n" + \
                    f"<strong>Sample Count </strong><code>{context.user_data['number_of_samples']}</code>\n\n" + \
                    f"<strong>Image Size </strong><code>{image_size}</code>\n\n" + \
                    f"Select the number of inference steps!\nThe <strong>higher</strong>" + \
                    f"the <strong>better</strong> the image!"
                await update.callback_query.edit_message_text(
                    text=message,
                    parse_mode="HTML",
                    reply_markup=inference_steps()
                )
            else:
                message = \
                    f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n" + \
                    f"<strong>Sample Count </strong><code>{context.user_data['number_of_samples']}</code>\n\n" + \
                    f"<strong>Image Size </strong><code>{image_size}</code>\n\n" + \
                    f"Select the number of inference steps!\nThe <strong>higher</strong>" + \
                    f"the <strong>better</strong> the image!"
                await update.callback_query.edit_message_text(
                    text=message,
                    parse_mode="HTML",
                    reply_markup=inference_steps()
                )
            context.user_data['image_width'] = int(image_size.split("x")[0])
            context.user_data['image_height'] = int(image_size.split("x")[1])
        if query.data.startswith('infs='):
            inference_steps_num = query.data.split("infs=")[1]
            if update.message is None:
                message = \
                    f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n" + \
                    f"<strong>Sample Count </strong><code>{context.user_data['number_of_samples']}</code>\n\n" + \
                    f"<strong>Image Size </strong>" + \
                    f"<code>{context.user_data['image_width']}x{context.user_data['image_height']}</code>\n\n" + \
                    f"<strong>Inference Steps </strong><code>{inference_steps_num}</code>\n\n" + \
                    f"Please reply to this message with the prompt you would like the bot to use!"
                await update.callback_query.edit_message_text(
                    text=message,
                    parse_mode="HTML",
                    reply_markup=None
                )
            else:
                message = \
                    f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n" + \
                    f"<strong>Sample Count </strong><code>{context.user_data['number_of_samples']}</code>\n\n" + \
                    f"<strong>Image Size </strong>" + \
                    f"<code>{context.user_data['image_width']}x{context.user_data['image_height']}</code>\n\n" + \
                    f"<strong>Inference Steps </strong><code>{inference_steps_num}</code>\n\n" + \
                    f"Please reply to this message with the prompt you would like the bot to use!"
                await update.callback_query.edit_message_text(
                    text=message,
                    parse_mode="HTML",
                    reply_markup=None
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
            elif type(image[1]) is list:
                await update.callback_query.message.reply_media_group(
                    media=[InputMediaPhoto(media=x) for x in image[1]],
                )
                response_message = await update.callback_query.message.reply_caption(
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
            elif type(image[1]) is list:
                await update.message.reply_media_group(
                    media=[InputMediaPhoto(media=x) for x in image[1]],
                )
                response_message = await update.message.reply_caption(
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
                context.user_data['tti_response_message'] = response_message.message_id

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
                    response_message = \
                        f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n"
                    await update.message.delete()
                    await update.message.reply_to_message.edit_text(
                        text=f"You have selected <strong>{context.user_data['selected_model_name']}</strong>\n\n<strong>User Prompt</strong>\n" + user_input + "\n\n<strong>\nPlease reply to this message once more to set the negative prompt you would like the AI to use!</strong>\n<strong>Or reply with - to use the default negative prompt</strong>",
                        parse_mode="HTML",
                        reply_markup=None
                    )
                    context.user_data['waiting_for_prompt'] = False
                    context.user_data['pos_prompt'] = user_input
                    context.user_data['waiting_for_neg_prompt'] = True

    def run(self):
        """Run the bot"""
        self.app.run_polling()


def run_app(token: str, image_api: TextToImageAsynchronous) -> ApplicationBuilder:
    bot = NexVerse(token, image_api)
    bot.run()
