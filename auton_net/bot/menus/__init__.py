from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from .developer_panel import (
    developer_panel_main,
    developer_panel_register,
    developer_panel_is_anonymous
)


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
