from aiogram import types
from created_bot import dp


async def echo_send(message: types.Message):
    if message.text == 'Добрый день!':
        await message.reply('И вам добрый день!')

def register_hendlers_others(dp: dp):
    dp.register_message_handler(echo_send)

