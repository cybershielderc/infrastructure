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
                
            ]
        ]
    )
