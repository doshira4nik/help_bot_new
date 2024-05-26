from aiogram.utils.keyboard import InlineKeyboardBuilder

def link_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text='Скачать видео из YouTube', url='https://ru.savefrom.net/240/')
    kb.button(text='Википедия', url='https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
    kb.button(text='w3schools', url='https://www.w3schools.com/python/default.asp')
    kb.button(text='aiogram docs', url='https://mastergroosha.github.io/aiogram-3-guide/')
    kb.adjust(2,2)
    return kb.as_markup()