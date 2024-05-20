from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def developer_panel_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🛠️ Seller Panel 🧾", callback_data="ignore_0xdead")],
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
                    "❌ No, I'm not a seller!", callback_data="mp_1"
                )
            ]
        ]
    )


def developer_panel_is_anonymous() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✅ Yes", callback_data="dev_reg#anon>>yes"
                ),
                InlineKeyboardButton(
                    "❌ No", callback_data="dev_reg#anon>>no"
                )
            ]
        ]
    )
