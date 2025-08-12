from aiogram.fsm.state import State, StatesGroup


class EncodeState(StatesGroup):
    photo = State()
    secret_key = State()
