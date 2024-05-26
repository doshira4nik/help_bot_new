from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from keyboards.reply import *
from keyboards.inline import *
import logging
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

#ОСНОВА
async def apps_handler(msg: Message, bot: Bot):
    await msg.answer(text="Вот список полезных приложений!\nХочешь предложить своё? Напиши владельцу!\nЧтобы узнать контакт, перейди в главное меню и нажми на кнопку <u>Обратная связь</u>", reply_markup=apps_keyboard())

#VKMP
async def upload_vkmp(msg: Message):
    await msg.answer(text="Ожидайте, файл подгружается, пока можете заняться чем-то другим")
    file_ids = []
    with open("VKMP.apk", "rb") as vkmp_apk:
        result = await msg.answer_document(
            BufferedInputFile(
                vkmp_apk.read(),
                filename="VKMP.apk"
            ),
            caption="Загрузчик VKMP\nVKMP - приложение для прослушивания музыки из вашей библиотеки ВКонтакте <b>абсолютно бесплатно, в фоновом режиме</b>.\nСсылка на офиц. сайт: https://vkmp.app"
        )
        file_ids.append(result.document[-1].file_id)

#TIME! MEMO!
async def upload_time(msg: Message):
    await msg.answer(text="Ожидайте, файл подгружается, пока можете заняться чем-то другим")
    file_ids = []
    with open("Time_Memo.apk", "rb") as time_apk:
        result = await msg.answer_document(
            BufferedInputFile(
                time_apk.read(),
                filename="Time_Memo.apk"
            ),
            caption="Time! Memo! - часы поверх экрана, и не только часы.\nСсылка на офиц. сайт/страницу Play Market: https://play.google.com/store/apps/details?id=wan.util.showtime"
        )
        file_ids.append(result.document[-1].file_id)

#кликер
async def upload_clicker(msg: Message):
    await msg.answer(text="Ожидайте, файл подгружается, пока можете заняться чем-то другим")
    file_ids = []
    with open("Auto_Clicker.apk", "rb") as click_apk:
        result = await msg.answer_document(
            BufferedInputFile(
                click_apk.read(),
                filename="Auto_Clicker.apk"
            ),
            caption="Auto Clicker - название говорит само за себя, один из лучших кликеров.\nСсылка на офиц. сайт/страницу Play Market: https://play.google.com/store/apps/details?id=com.truedevelopersstudio.automatictap.autoclicker"
        )
        file_ids.append(result.document[-1].file_id)

#i drive XD
async def upload_drive(msg: Message):
    await msg.answer(text="Ожидайте, файл подгружается, пока можете заняться чем-то другим")
    file_ids = []
    with open("drive_ahead.apk", "rb") as drive_apk:
        result = await msg.answer_document(
            BufferedInputFile(
                drive_apk.read(),
                filename="drive_ahead.apk"
            ),
            caption="Drive Ahead - в паре слов, легендарная игра, именно тут .apk старой версии, т.к. новую не все одобрят\nСсылка на скачивание этой версии: <del>утеряна</del>"
        )
        file_ids.append(result.document[-1].file_id)

#minecraft
async def upload_mine(msg: Message):
    await msg.answer(text="Ожидайте, файл подгружается, пока можете заняться чем-то другим")
    file_ids = []
    with open("minecraftpe1.20.60.04.apk", "rb") as mine_apk:
        result = await msg.answer_document(
            BufferedInputFile(
                mine_apk.read(),
                filename="minecraftpe1.20.60.04.apk"
            ),
            caption="Minecraft 1.20.60.04 - лучшая версия из новых для модов\nСсылка на скачивание этой версии: <del>утеряна</del>"
        )
        file_ids.append(result.document[-1].file_id)