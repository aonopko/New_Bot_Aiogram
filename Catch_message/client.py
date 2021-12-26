from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from created_bot import bot
from Keyboard.klient_kb import kb_client
from data_base import sqlite_db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def bot_menu_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=kb_client)


async def delivery(message : types.Message):
    await bot.send_message(message.from_user.id, '1. Нова пошта - відправка щодено\n'
                                                 '2. Укрпошта - відправка пн-пт\n'
                                                 '3. Justin - відправка по суботах')


async def assortment(message : types.Message):
    item_db = await sqlite_db.add_basket()
    for ret in item_db:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}')
        await bot.send_message(message.from_user.id, text='Меню товару', reply_markup=InlineKeyboardMarkup().\
                                add(InlineKeyboardButton(f'Додати у кошик', callback_data=f'add {ret[4]}')))


def register_hendlers(dp : Dispatcher):
    dp.register_message_handler(bot_menu_command, commands=['start', 'help'])
    dp.register_message_handler(delivery, commands=['Доставка'])
    dp.register_message_handler(delivery, Text(equals='Доставка', ignore_case="/"))
    dp.register_message_handler(assortment, commands=['В наявності'])
    dp.register_message_handler(assortment, Text(equals='В наявності', ignore_case="/"))





