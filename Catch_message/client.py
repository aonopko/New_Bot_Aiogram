from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from created_bot import bot
from Keyboard.klient_kb import kb_client
from Keyboard.inline_kb import inline_markup
from data_base import sqlite_db


async def bot_menu_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать!',
                           reply_markup=kb_client,)


async def delivery(message : types.Message):
    await bot.send_message(message.from_user.id, '1. Нова пошта - відправка щодено\n'
                                                '3. Justin - відправка по суботах\n'
                                                '2. Укрпошта - відправка пн-пт\n')


async def assortment(message : types.Message):
    await bot.send_message(message.from_user.id, 'Весь асортимент',
                           reply_markup=inline_markup)


async def stock(message: types.Message):
    await sqlite_db.get_all_assortment(message)

def register_hendlers(dp: Dispatcher):
    dp.register_message_handler(bot_menu_command, commands=['start', 'help'])
    dp.register_message_handler(delivery, commands=['\U0001f69A  '+'Доставка'])
    dp.register_message_handler(delivery, Text(equals='\U0001f69A  '+'Доставка', ignore_case="/"))
    dp.register_message_handler(assortment, commands=['\U0001f440  '+'Весь асортимент'])
    dp.register_message_handler(assortment, Text(equals='\U0001f440  '+'Весь асортимент', ignore_case="/"))
    dp.register_message_handler(stock, commands=['\U0001f9E6  '+ 'В наявності'])
    dp.register_message_handler(stock, Text(equals='\U0001f9E6  ' + 'В наявності', ignore_case="/"))






