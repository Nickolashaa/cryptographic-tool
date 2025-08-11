from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from ..keyboards import start_keyboard


start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        text="Приветствую! Я умею шифровать и расшифровывать данные.",
        reply_markup=start_keyboard,
    )
