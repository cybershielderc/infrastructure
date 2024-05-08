from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start_menu_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🛠️ Services 🧾", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Text-to-Image (TTI)", callback_data="m1"),
                # InlineKeyboardButton("Image-to-Image (WIP)", callback_data="ignore_0xdead"),  # "image_to_image"),
                # InlineKeyboardButton("AI Assistant (WIP)", callback_data="ignore_0xdead"),  # "initiate_chat"),
            ]
        ]
    )
