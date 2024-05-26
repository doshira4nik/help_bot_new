from aiogram.types import  Message
from aiogram.fsm.context import  FSMContext
from states import WorkState
from aiogram import Dispatcher
from aiogram.filters import Command

async def  off_handler(msg: Message, state: FSMContext):
    await msg.answer('Бот отключен. Для запуска введите команду /on')
    await state.set_state(WorkState.OFF)

async def  sleep_handler(msg: Message, state: FSMContext):
    await msg.answer('Включи бота!!! /on')

async def  on_handler(msg: Message, state: FSMContext):
    await msg.answer('Бот был запущен!')
    await state.clear() 

def reg_st_handler(dp: Dispatcher):
    dp.message.register(on_handler, WorkState.OFF, Command(commands='on'))
    dp.message.register(sleep_handler, WorkState.OFF)
    dp.message.register(off_handler, Command(commands='off'))