from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def developer_panel_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🛠️ Developer Panel 🧾", callback_data="ignore_0xdead")],
            [[InlineKeyboardButton("Stats", callback_data="mp_dev_stats")]]
        ]
    )
