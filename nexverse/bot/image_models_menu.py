from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def ai_models_image_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Realism", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("MidJourney v4", callback_data="ai>img>model>selection#//midjourney"),
                InlineKeyboardButton("Realistic Vision v4", callback_data="ai>img>model>selection#//rvision"),
                InlineKeyboardButton("Juggernaut XL", callback_data="ai>img>model>selection#//juggernaut")
            ],
            [InlineKeyboardButton("Anime", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Anything v4", callback_data="ai>img>model>selection#//anything"),
                InlineKeyboardButton("Dark Sushi 2.5D", callback_data="ai>img>model>selection#//darksushi"),
                InlineKeyboardButton("Sakura v3", callback_data="ai>img>model>selection#//sakura")
            ],
            [InlineKeyboardButton("NSFW", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Deliberate", callback_data="ai>img>model>selection#//deliberate"),
                InlineKeyboardButton("Perfect Deli", callback_data="ai>img>model>selection#//perfectdeli"),
                InlineKeyboardButton("Mix Appfactory", callback_data="ai>img>model>selection#//mixappfactory"),
                InlineKeyboardButton("Dark Appfactory (Anime)",
                                     callback_data="ai>img>model>selection#//nsfw_darkappfactory")
            ],
            [InlineKeyboardButton("Artistic", callback_data="ignore_0xdead")],
            [InlineKeyboardButton("Work In Progress!", callback_data="ignore_0xdead")],

        ]
    )
