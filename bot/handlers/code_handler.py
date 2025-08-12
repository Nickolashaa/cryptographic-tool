from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, BufferedInputFile
from aiogram.fsm.context import FSMContext
from ..states import CodeState
from services import CryptoGraphicService, FileService
from ..keyboards import end_keyboard, to_main_menu


code_router = Router()


@code_router.callback_query(F.data == "code")
async def start_code(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    message = await callback.message.answer(
        text="Пришлите информацию для кодировки (доступен только текстовый формат). Как только закончите, нажмите кнопку Завершить",
        reply_markup=end_keyboard,
    )
    await callback.message.delete()
    await state.set_state(CodeState.text)
    await state.update_data(
        text="",
        last_message_id=message.message_id,
    )


@code_router.message(CodeState.text)
async def add_text(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    await message.bot.delete_message(
        chat_id=int(message.from_user.id),
        message_id=int(data["last_message_id"]),
    )
    answer_message = await message.answer(
        text="Информация записана.",
        reply_markup=end_keyboard,
    )
    await state.update_data(
        text=data["text"] + " " + message.text,
        last_message_id=answer_message.message_id,
    )


@code_router.callback_query(F.data == "end_code")
async def add_secret_key(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer(
        text=(
            "Информация готова к шифрованию. Укажите секретный ключ.\n"
            "Информацию сможет получить только тот, кто знает этот ключ.\n"
            "Ключом может быть любая строка символов. Например: Ra9"
        )
    )
    await state.set_state(CodeState.secret_key)


@code_router.message(CodeState.secret_key)
async def code(message: Message, state: FSMContext) -> None:
    await state.update_data(secret_key=message.text)
    data = await state.get_data()
    await state.clear()
    await message.answer("Начинаю шифрование.")
    file = FileService.get_random_file()
    secret_file_bytes = CryptoGraphicService.code(
        file=file,
        text=data["text"],
        secret_key=data["secret_key"],
    )
    secret_file = BufferedInputFile(
        secret_file_bytes, filename="encrypted_image.jpg")
    await message.answer("Ваша информация зашифрована и удалена с сервера.")
    await message.answer_photo(
        photo=secret_file,
        caption=(
            "В этой картинке зашифрована ваша информация.\n"
            "Передайте получателю эту картинку и секретный ключ."
        ),
        reply_markup=to_main_menu,
    )
