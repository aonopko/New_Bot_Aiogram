from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from created_bot import bot
from Keyboard.klient_kb import kb_client
from Keyboard.Inline_kb import inline_markup
#from data_base import sqlite_db


async def bot_menu_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать!',
                           reply_markup=kb_client,
                           )


async def delivery(message : types.Message):
    await bot.send_message(message.from_user.id, '1. Нова пошта - відправка щодено\n'
                                                '3. Justin - відправка по суботах\n'
                                                '2. Укрпошта - відправка пн-пт\n')


async def assortment(message : types.Message):
    await bot.send_message(message.from_user.id, '\U0001f917'+'Меню товара',
                           reply_markup=inline_markup)


def register_hendlers(dp: Dispatcher):
    dp.register_message_handler(bot_menu_command, commands=['start', 'help'])
    dp.register_message_handler(delivery, commands=['Доставка'])
    dp.register_message_handler(delivery, Text(equals='Доставка', ignore_case="/"))
    dp.register_message_handler(assortment, commands=['В наявності'])
    dp.register_message_handler(assortment, Text(equals='В наявності', ignore_case="/"))





