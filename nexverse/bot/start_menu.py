from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start_menu_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("💸 Wallet & Balance 💸", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Connect Wallet", callback_data="wallet_connect"),
                InlineKeyboardButton("$GENAI Balance (WIP)", callback_data="csl_balance"),
                InlineKeyboardButton("My Wallet", callback_data="display_wallet_address")
            ],
            [InlineKeyboardButton("🛠️ Services 🧾", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Text-to-Image (TTI)", callback_data="text_to_image"),
                InlineKeyboardButton("Image-to-Image (WIP)", callback_data="ignore_0xdead"),  # "image_to_image"),
                InlineKeyboardButton("AI Assistant", callback_data="ignore_0xdead"),  # "initiate_chat"),
            ]
        ]
    )
