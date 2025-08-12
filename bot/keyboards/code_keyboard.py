from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


end_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Завершить', callback_data='end_code'
            )
        ],
    ]
)
