from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='В главое меню', callback_data='main'
            )
        ],
    ]
)
