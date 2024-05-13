from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def developer_panel_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🛠️ Developer Panel 🧾", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("🛠️ Stats 🧾", callback_data="mp_dev_stats"),
                InlineKeyboardButton(" 🧾Orders 🧾", callback_data="mp_dev_orders"),
                InlineKeyboardButton("💸 Awaiting Funds 🧾", callback_data="mp_dev_funds"),
            ],
            [InlineKeyboardButton("🔙 Back 🔙", callback_data="mp_1")],
        ]
    )


def developer_panel_register() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✅ Yes, Register me!", callback_data="mp_dev_start_registration"
                ),
                InlineKeyboardButton(
                    "❌ No, I'm not a developer!", callback_data="mp_1"
                )
            ]
        ]
    )


def developer_panel_is_anonymous() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✅ Yes, I'd like to remain anonymous", callback_data="mp_dev_enable_anonymity"
                ),
                InlineKeyboardButton(
                    "❌ No, I'd like to be seen", callback_data="mp_dev_disable_anonymity"
                )
            ]
        ]
    )
