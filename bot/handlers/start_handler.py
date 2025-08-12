from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from ..keyboards import start_keyboard


start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        text="Приветствую! Я умею шифровать и расшифровывать данные.",
        reply_markup=start_keyboard,
    )

@start_router.callback_query(F.data == "main")
async def start(callback: CallbackQuery) -> None:
    await callback.answer()
    await callback.message.answer(
        text="Приветствую! Я умею шифровать и расшифровывать данные.",
        reply_markup=start_keyboard,
    )