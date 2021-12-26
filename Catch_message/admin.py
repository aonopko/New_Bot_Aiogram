from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from Keyboard import admin_kb
from created_bot import bot
from data_base import sqlite_db


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    articul = State()
    quantity = State()


async def admin_panel(message: types.Message):
    await bot.send_message(message.from_user.id, 'АДМІНКА АКТИВОВАНА',
                           reply_markup=admin_kb.kb_admin)


async def load_item(message: types.Message):
    await FSMAdmin.photo.set()
    await bot.send_message(message.from_user.id, 'Додайте фото')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Фото завантажено')
    await bot.send_message(message.from_user.id, 'Додайте назву товару')


async def load_name(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Назва товару додано')
    await bot.send_message(message.from_user.id, 'Додайте опис товару')


async def load_description(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Опис товру додано')
    await bot.send_message(message.from_user.id, 'Додайте вартість товару')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = str(message.text)
    await FSMAdmin.next()
    await message.reply('Вартість додано')
    await bot.send_message(message.from_user.id, 'Додайте артикул товару')


async def load_articul(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['articul'] = str(message.text)
    await FSMAdmin.next()
    await message.reply('Артикул додано')
    await bot.send_message(message.from_user.id, "Додайте об'єм товару")


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['quantity'] = str(message.text)
    await message.reply('Товар додано')
    try:
        await sqlite_db.sql_add_items(state)
    except:
        await bot.send_message(message.from_user.id, 'Товар Існує')
    await state.finish()


async def log_out(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Вихід - ОК')


def register_handlrs_admin(dp: Dispatcher):
    dp.register_message_handler(admin_panel, commands=['moderator'])
    dp.register_message_handler(load_item, commands=['Завантажити товар'])
    dp.register_message_handler(load_item, Text(equals=['Завантажити товар'], ignore_case="/"))
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_articul, state=FSMAdmin.articul)
    dp.register_message_handler(load_quantity, state=FSMAdmin.quantity)
    dp.register_message_handler(log_out, state="*", commands=['exit'])