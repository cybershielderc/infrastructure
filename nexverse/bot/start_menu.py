from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start_menu_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("💸 Wallet & Balance 💸", callback_data="ignore_0xdead")],
            
        ]
    )
