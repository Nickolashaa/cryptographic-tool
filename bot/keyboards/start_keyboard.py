from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Зашифровать данные', callback_data='code'
            )
        ],
        [
            InlineKeyboardButton(
                text='Расшифровать данные', callback_data='encode'
            )
        ],
    ]
)
