from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def ai_models_image_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Realism", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("MidJourney v4", callback_data="text_midjourney"),
                InlineKeyboardButton("Realistic Vision v4", callback_data="text_rvision"),
                InlineKeyboardButton("Juggernaut XL", callback_data="text_juggernaut")
            ],
            [InlineKeyboardButton("Anime", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Anything v4", callback_data="text_anything"),
                InlineKeyboardButton("Dark Sushi 2.5D", callback_),
                InlineKeyboardButton(),
            ]
        ]
    )
