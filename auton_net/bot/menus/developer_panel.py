from typing import Any

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def developer_panel_main() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🛠️ Seller Panel 🧾", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("🛠️ Stats 🧾", callback_data="developer_stats"),
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
    if rating < 0 or rating > 5:
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
                InlineKeyboardButton(text=f"{determine_rating(statistics[4])}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Are you verified?", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{'Yes ✅' if statistics[5] else 'No ❌'}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Wallet verified?", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{'Yes ✅' if statistics[12] else 'No ❌'}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Are you anonymous?", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{'Yes ✅' if statistics[6] else 'No ❌'}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Your nickname is", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[7]}", callback_data="ignore_0xdead")
            ] if statistics[6] else [],
            # Line Two
            [InlineKeyboardButton(text="Order Statistics", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton(text="Completed", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[8]}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Open", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[9]}", callback_data="ignore_0xdead")
            ],
            [
                InlineKeyboardButton(text="Rejected", callback_data="ignore_0xdead"),
                InlineKeyboardButton(text=f"{statistics[10]}", callback_data="ignore_0xdead")
            ],
            [InlineKeyboardButton(text="Your Seller UUID is", callback_data="ignore_0xdead")],
            [InlineKeyboardButton(text=f"{statistics[13]}", callback_data="ignore_0xdead")],
            [InlineKeyboardButton("🔙 Back 🔙", callback_data="mp_dev")],
        ]
    )
