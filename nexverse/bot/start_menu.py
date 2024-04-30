from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start_menu_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("💸 Wallet & Balance 💸", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Connect Wallet", callback_data="wallet_connect"),
                InlineKeyboardButton("$CSL Balance (WIP)", callback_data="csl_balance"),
                InlineKeyboardButton("My Wallet", callback_data="display_wallet_address")
            ]
        ]
    )
