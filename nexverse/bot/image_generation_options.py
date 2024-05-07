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
            InlineKeyboardButton('40', callback_data='infs=40')
        ],
        [
            InlineKeyboardButton('50', callback_data='infs=50'),
            InlineKeyboardButton('60', callback_data='infs=60'),
            InlineKeyboardButton('70', callback_data='infs=70'),
            InlineKeyboardButton('80', callback_data='infs=80')
        ],
        [
            InlineKeyboardButton('90', callback_data='infs=90'),
            InlineKeyboardButton('100', callback_data='infs=100'),
            InlineKeyboardButton('110', callback_data='infs=110'),
            InlineKeyboardButton('120', callback_data='infs=120')
        ],
        [
            InlineKeyboardButton('130', callback_data='infs=130'),
            InlineKeyboardButton('140', callback_data='infs=140'),
            InlineKeyboardButton('150', callback_data='infs=150'),
            InlineKeyboardButton('160', callback_data='infs=160')
        ],
        [
            InlineKeyboardButton('170', callback_data='infs=170'),
            InlineKeyboardButton('180', callback_data='infs=180'),
            InlineKeyboardButton('190', callback_data='infs=190'),
            InlineKeyboardButton('200', callback_data='infs=200')
        ],
    ])


def numberof_samples() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton('1', callback_data='samples=1'),
            InlineKeyboardButton('2', callback_data='samples=2'),
            InlineKeyboardButton('3', callback_data='samples=3'),
            InlineKeyboardButton('4', callback_data='samples=4'),
        ]
    ])
