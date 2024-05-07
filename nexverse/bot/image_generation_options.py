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
            InlineKeyboardButton('20', callback_data='infs=20'),
            InlineKeyboardButton('40', callback_data='infs=40'),
            InlineKeyboardButton('60', callback_data='infs=60'),
            InlineKeyboardButton('80', callback_data='infs=80')
        ],
        [InlineKeyboardButton('One-time Payment of 500 $GEN to use!', callback_data='ignore_0xdead')],
        [
            InlineKeyboardButton('100', callback_data='infs=100'),
            InlineKeyboardButton('120', callback_data='infs=120'),
            InlineKeyboardButton('140', callback_data='infs=140'),
            InlineKeyboardButton('160', callback_data='infs=160')
        ],
        [InlineKeyboardButton('One-time Payment of 1,000 $GEN to use!', callback_data='ignore_0xdead')],
        [
            InlineKeyboardButton('200', callback_data='infs=200'),
            InlineKeyboardButton('300', callback_data='infs=300'),
            InlineKeyboardButton('400', callback_data='infs=400'),
            InlineKeyboardButton('500', callback_data='infs=500')
        ],
        [InlineKeyboardButton('One-time Payment of 2,000 $GEN to use!', callback_data='ignore_0xdead')],
        [
            InlineKeyboardButton('600', callback_data='infs=600'),
            InlineKeyboardButton('700', callback_data='infs=700'),
            InlineKeyboardButton('800', callback_data='infs=800'),
            InlineKeyboardButton('1,000', callback_data='infs=1000')
        ],
        [InlineKeyboardButton('One-time Payment of 3,000 $GEN to use!', callback_data='ignore_0xdead')],
        [
            InlineKeyboardButton('1,500', callback_data='infs=1,500'),
            InlineKeyboardButton('2,000', callback_data='infs=2,000'),
            InlineKeyboardButton('2,500', callback_data='infs=2,500'),
            InlineKeyboardButton('3,000', callback_data='infs=3,000')
        ],
        [InlineKeyboardButton('One-time Payment of 5,000 $GEN to use!', callback_data='ignore_0xdead')],
        [
            InlineKeyboardButton('5,000', callback_data='infs=5000'),
            InlineKeyboardButton('6,000', callback_data='infs=6000'),
            InlineKeyboardButton('8,000', callback_data='infs=8000'),
            InlineKeyboardButton('10,000', callback_data='infs=10000')
        ]
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
