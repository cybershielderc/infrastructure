from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def size_options() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton('512x512', callback_data='size=512x512'),
         InlineKeyboardButton('1024x1024', callback_data='size=1024x1024')
         ]
    ])


def inference_steps() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton('10', callback_data='infs=10'),
            InlineKeyboardButton('20', callback_data='infs=20'),
            InlineKeyboardButton('30', callback_data='infs=30'),
        ],
        [
            InlineKeyboardButton('40', callback_data='infs=40'),
            InlineKeyboardButton('50', callback_data='infs=50'),
            InlineKeyboardButton('60', callback_data='infs=60'),
        ],
        [
            InlineKeyboardButton('70', callback_data='infs=70'),
            InlineKeyboardButton('80', callback_data='infs=80'),
            InlineKeyboardButton('90', callback_data='infs=90'),
        ],
    ])


def numberof_samples() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton('')
        ]
    ])
