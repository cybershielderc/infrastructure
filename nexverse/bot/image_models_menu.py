from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def ai_models_image_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Realism", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("MidJourney v4",
                                     callback_data="ai>img>model>selection#//realism1#CNAME#MidJourney V4"),
                InlineKeyboardButton("Realistic Vision v4",
                                     callback_data="ai>img>model>selection#//realism2#CNAME#Realistic Vision V4"),
                InlineKeyboardButton("Juggernaut XL",
                                     callback_data="ai>img>model>selection#//realism3#CNAME#Juggernaut XL")
            ],
            [InlineKeyboardButton("Anime", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Anything v4", callback_data="ai>img>model>selection#//anime1#CNAME#Anything V4"),
                InlineKeyboardButton("Dark Sushi 2.5D",
                                     callback_data="ai>img>model>selection#//anime2#CNAME#Dark Sushi 2.5D"),
                InlineKeyboardButton("Sakura v3", callback_data="ai>img>model>selection#//anime3#CNAME#Sakura v3")
            ],
            [InlineKeyboardButton("NSFW", callback_data="ignore_0xdead")],
            [
                InlineKeyboardButton("Deliberate", callback_data="ai>img>model>selection#//nsfw1#CNAME#Deliberate"),
                InlineKeyboardButton("Perfect Deli", callback_data="ai>img>model>selection#//nsfw2#CNAME#Perfect Deli"),
                InlineKeyboardButton("Mix Appfactory",
                                     callback_data="ai>img>model>selection#//nsfw3#CNAME#Mix Appfactory"),
                InlineKeyboardButton("Dark Appfactory (Anime)",
                                     callback_data="ai>img>model>selection#//nsfw4#CNAME#Dark Appfactory")
            ],
            # [InlineKeyboardButton("Artistic", callback_data="ignore_0xdead")],
            # [InlineKeyboardButton("Work In Progress!", callback_data="ignore_0xdead")],

        ]
    )
