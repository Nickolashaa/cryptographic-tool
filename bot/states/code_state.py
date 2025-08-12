from aiogram.fsm.state import State, StatesGroup


class CodeState(StatesGroup):
    last_message_id = State()
    text = State()
    secret_key = State()
