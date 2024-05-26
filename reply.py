from aiogram.utils.keyboard import ReplyKeyboardBuilder

def main_menu_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Что умеет бот?')
    keyboard_builder.button(text='Обратная связь')
    keyboard_builder.button(text='Полезные ссылки')
    keyboard_builder.button(text='Приложения')
    keyboard_builder.button(text='Озвучка')
    keyboard_builder.button(text='Переводчик')
    keyboard_builder.adjust(2,2,2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder = 'шо эта?'
    )

def fake_menu_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Что умеет бот?')
    keyboard_builder.button(text='Обратная связь')
    keyboard_builder.button(text='Полезные ссылки')
    keyboard_builder.button(text='Приложения')
    keyboard_builder.button(text='Озвучка')
    keyboard_builder.button(text='Переводчик')
    keyboard_builder.button(text='Ты сдурел а?')
    keyboard_builder.adjust(2,2,2,1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder = 'это фейк!! тссс..'
    )
def restart_trans_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Повторить')
    keyboard_builder.button(text='Вернуться в меню')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder = 'еще раз?'
    )
def apps_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='VKMP')
    keyboard_builder.button(text='Time! Memo!')
    keyboard_builder.button(text='Auto Clicker')
    keyboard_builder.button(text='top secret')
    keyboard_builder.button(text='Вернуться в меню')
    keyboard_builder.adjust(2,2,1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder = 'Выберите приложение'
    )

def secret_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Drive Ahead')
    keyboard_builder.button(text='Minecraft')
    keyboard_builder.button(text='Вернуться')
    keyboard_builder.adjust(2,1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder = 'выбирай!'
    )

def escape_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Вернуться в меню')
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder = 'а что еще то?'
    )

def what_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Почему?')
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder = 'потому'
    )
def choco_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.button(text='Ну и ладно..')
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder = 'а?'
    )