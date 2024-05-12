from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def developer_panel_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🛠️ Marketplace 🧾", callback_data="ignore_0xdead")],
        ]
    )
