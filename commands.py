from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot : Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начать'
        ),
        BotCommand(
            command='menu',
            description='Меню'
            ),
        BotCommand(
            command='on',
            description='Activation bot'
            ),
        BotCommand(
            command='off',
            description='Deactivation bot')
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())