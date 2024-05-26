from googletrans import Translator
from aiogram.types import Message
from states import TranslationState
from aiogram.fsm.context import FSMContext
from keyboards.reply import restart_trans_keyboard
translator = Translator()
async def translate_handler(msg: Message, state: FSMContext):
    await msg.answer('Введите текст для перевода:')
    state.set_state(TranslationState.ON)


async def translate_input(msg: Message, state: FSMContext):
    translate_result = translator.translate(msg.text, dest='ru')
    await msg.reply(text = translate_result.text)
    await msg.answer(text='Хотите повторить?', reply_markup=restart_trans_keyboard())
    state.clear()