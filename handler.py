from aiogram import Bot, F
from aiogram.types import Message
from keyboards.reply import *
from keyboards.inline import *
from aiogram import html

async def start_handler( msg: Message, bot: Bot):
    await msg.answer(f"Приветствую, {html.bold(html.quote(msg.from_user.full_name))}! <b>я - ваш бот ассистент</b>.\nМоя задача помочь вам и хоть немного облегчить вашу жизнь", reply_markup = main_menu_keyboard())

async def help_handler(msg: Message, bot: Bot):
    await msg.answer(text="Функции и возможности бота:\n1.Полезные ссылки\n2.Переводчик\n3.Полезные приложения\n4.Озвучивание текста\nТакже имеется <u>Обратная связь с разработчиком</u>", reply_markup=escape_keyboard())

async def feedback_handler(msg: Message, bot: Bot):
    await msg.answer(text="Хотите связаться с создателем бота?\nВ таком случае вам необходимо написать ему: @aggresive_person\nПисать <b>строго</b> по форме:\n1.Причина\n2.Решение/Идея\n3.Слова от себя (необязательно!)\nНи в коем случае <u>не ведитесь на фейки, всегда достоверно проверяйте информацию!</u>", reply_markup=main_menu_keyboard())

async def secret_handler(msg: Message, bot: Bot):
    await msg.answer(text="Ты зашел в секретное место, тут находятся легендарные, ну и не особо игры", reply_markup=secret_keyboard())

async def link_handler(msg: Message, bot: Bot):
    await msg.answer(text='Известные ссылки:\n1.SaveFrom - скачивание видео из ютуба\n2.Википедия - свободная энциклопедия\n3.w3school - документация по разным языкам программирования\n4.Aiogram docs - понятная базовая документация по aiogram\nХочешь добавить что-то своё? Пиши владельцу!', reply_markup=link_keyboard())

async def esc_apps_handler(msg: Message, bot: Bot):
    await msg.answer(text='Меню приложений:', reply_markup=apps_keyboard())

async def res_menu_handler(msg: Message, bot: Bot):
    await msg.answer(text='Меню:', reply_markup=main_menu_keyboard())

async def error_handler(msg: Message, bot: Bot):
    await msg.answer(text=f'Я вас не понимаю..', reply_markup=what_keyboard())

async def photo_handler(msg: Message, bot: Bot):
    await msg.reply('Крутая пикча!')

async def what_handler(msg: Message, bot: Bot):
    await msg.answer(text="Да потому что ты несешь какую-то чертовщину!!!", reply_markup=choco_keyboard())

async def choco_handler(msg: Message, bot: Bot):
    await msg.answer(text="Ну и шоколадно !\nВозврат в главное меню..", reply_markup=fake_menu_keyboard())

async def angry_handler(msg: Message, bot: Bot):
    await msg.answer(text="Я уже <b>зол</b>!!\nНо культурно все еще получится, перестань", reply_markup=main_menu_keyboard())

async def esc_handler(msg: Message, bot: Bot):
    await msg.answer(text="Вы вернулись на главное меню:", reply_markup=main_menu_keyboard())