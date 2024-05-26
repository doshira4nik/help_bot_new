from aiogram import Bot, Dispatcher, F
from handler import *
import asyncio
from aiogram.filters import Command
from commands import set_commands
from state_handlers import *
from audio import audio_handler
from translate import *
from apps_handlers import *
from settings import settings
from states import TranslationState


async def start():
    bot = Bot(token=settings.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    dp.startup.register(set_commands)
    reg_st_handler(dp)
    #other
    dp.message.register(audio_handler, F.text=='Озвучка')
    dp.message.register(apps_handler, F.text=='Приложения')
    dp.message.register(help_handler, F.text=='Что умеет бот?')
    dp.message.register(feedback_handler, F.text=='Обратная связь')
    dp.message.register(translate_handler, F.text=='Переводчик')
    dp.message.register(translate_handler, F.text=='Повторить')
    dp.message.register(translate_input, TranslationState.ON)
    dp.message.register(link_handler, F.text=='Полезные ссылки')
    dp.message.register(esc_handler, F.text=='Вернуться в меню')
    dp.message.register(esc_apps_handler, F.text=='Вернуться')
    #joke
    dp.message.register(what_handler, F.text=='Почему?')
    dp.message.register(choco_handler, F.text=='Ну и ладно..')
    dp.message.register(angry_handler, F.text=='Ты сдурел а?')
    #apps
    dp.message.register(secret_handler, F.text=='top secret')
    dp.message.register(upload_vkmp, F.text=='VKMP')
    dp.message.register(upload_time, F.text=='Time! Memo!')
    dp.message.register(upload_clicker, F.text=='Auto Clicker')
    dp.message.register(upload_mine, F.text=='Minecraft')
    dp.message.register(upload_drive, F.text=='Drive Ahead')
    #commands
    dp.message.register(res_menu_handler, Command(commands=['menu']))
    dp.message.register(start_handler, Command(commands=['start']))
    #other
    dp.message.register(photo_handler, F.photo)
    dp.message.register(error_handler)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



if __name__ == '__main__':
    asyncio.run(start())