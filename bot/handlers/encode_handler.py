from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from ..states import EncodeState
from services import CryptoGraphicService, FileService


encode_router = Router()


@encode_router.callback_query(F.data == "encode")
async def start_endcode(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(
        text="Пришлите фото для декодировки (фото, не документ).",
    )
    await state.set_state(EncodeState.photo)


@encode_router.message(EncodeState.photo)
async def get_photo(message: Message, state: FSMContext):
    try:
        photo_data = await FileService.photo_to_bytes(
            photo=message.photo[-1],
            bot=message.bot,
        )
        await state.update_data(photo=photo_data)
        await message.answer("Пришлите секретный ключ.")
        await state.set_state(EncodeState.secret_key)
    except Exception:
        await message.answer("Ошибка вводных данных")
        await state.clear()


@encode_router.message(EncodeState.secret_key)
async def decode(message: Message, state: FSMContext):
    await state.update_data(secret_key=message.text)
    data = await state.get_data()
    await state.clear()
    try:
        text = CryptoGraphicService.encode(
            file=data["photo"],
            secret_key=data["secret_key"],
        )
        await message.answer("Секретная информация:")
        await message.answer(text)
    except ValueError as e:
        await message.answer(str(e))
    except ValueError as e:
        await message.answer(str(e))