from typing import Any

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


def determine_rating(rating: float) -> str:
    if rating < 1 or rating > 5:
        raise ValueError("Rating must be between 1 and 5")
    full_stars = int(rating)
    remaining = rating - full_stars
    stars = "🌕" * full_stars
    if remaining >= 0.75:
        stars += "🌖"
    elif remaining >= 0.5:
        stars += "🌗"
    elif remaining >= 0.25:
        stars += "🌘"
    return stars.ljust(5, "🌑")


def developer_panel_statistics(
        statistics: list[Any]
) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            # Line One
            [InlineKeyboardButton(text="Accepted Budget Range", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton(text="Minimum (In USD)", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[0]}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Maximum (In USD)", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[1]}", callback_data="ignore_0xdead")
            ],
            # Line Two
            [InlineKeyboardButton(text="Accepted Timeframe Range", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton(text="Minimum (In Days)", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[2]}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Maximum (In Days)", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[3]}", callback_data="ignore_0xdead")
            ],
            # Rating
            [InlineKeyboardButton(text="Reputation", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton(text="Your Rating is", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[2]}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Maximum (In Days)", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[3]}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Maximum (In Days)", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[3]}", callback_data="ignore_0xdead")
            ],
        ]
    )
