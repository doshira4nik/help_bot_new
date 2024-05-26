from gtts import gTTS
from aiogram import Bot, F
from aiogram.types import Message
from keyboards.reply import *

async def audio_handler(msg: Message, bot: Bot):
    tts = gTTS(msg.text, lang='ru')
    tts.save(f'{msg.from_user.id}.mp3')
    await msg.answer_voice(open(f'{msg.from_user.id}.mp3', 'rb'))