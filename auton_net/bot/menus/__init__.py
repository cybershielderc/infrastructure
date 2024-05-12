from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from .

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
        [InlineKeyboardButton("👷 Developer Panel 👷", callback_data="mp_dev"),
         InlineKeyboardButton("🙋 Customer Panel 🙋", callback_data="mp_customer")]
    ])
