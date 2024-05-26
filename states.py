from aiogram.fsm.state import StatesGroup, State

class WorkState(StatesGroup):
    OFF = State()

class TranslationState(StatesGroup):
    ON = State()
    