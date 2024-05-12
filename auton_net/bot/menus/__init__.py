from telegram import InlineKeyboardButton, InlineKeyboardMarkup


# Small Menus
def start_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🛠️ Marketplace 🧾", callback_data="mp_1")],
        ]
    )


def marketplace_panel() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛠️ Marketplace 🧾", callback_data="ignore_0xdead")],
        [In]
    ])
