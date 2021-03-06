import sqlite3

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from loguru import logger

from Keyboard import admin_kb
from created_bot import bot
from data_base import sqlite_db

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG',
           rotation='10 KB', compression='zip')


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()
    quantity = State()
    articul = State()


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


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply('Назва товару додано')
    await bot.send_message(message.from_user.id, 'Додайте опис товару')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Опис товру додано')
    await bot.send_message(message.from_user.id, 'Додайте вартість товару')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['price'] = float(message.text)
        except ValueError:
            await message.reply('\U0001f6AB  ' + 'Ввели не коректне значення\n')
            await bot.send_message(message.from_user.id, '\U0000261D  ' + 'Потрібно ввести число')
        else:
            await FSMAdmin.next()
            await message.reply('Вартість додано')
            await bot.send_message(message.from_user.id, "Додайте об'єм товару")


async def load_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['quantity'] = int(message.text)
        except ValueError:
            await message.reply('\U0001f6AB  ' + 'Ввели не коректне значення\n')
            await bot.send_message(message.from_user.id, '\U0000261D  ' + 'Потрібно ввести число')
        else:
            await FSMAdmin.next()
            await message.reply("Об'єм додано")
            await bot.send_message(message.from_user.id, "Додайте артикул товару")


async def load_articul(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['articul'] = str(message.text)
    try:
        await sqlite_db.sql_add_items(state)
    except sqlite3.IntegrityError:
        await bot.send_message(message.from_user.id, '\U0001f6AB  '+' УВАГА!!! Товар Існує')
        logger.warning('Спроба добавити існуючий товар')
    else:
        await message.reply('Товар додано')
    await state.finish()


async def log_out(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Вихід - ОК')


def register_handlrs_admin(dp: Dispatcher):
    dp.register_message_handler(admin_panel, commands=['moderator'], state=None)
    dp.register_message_handler(load_item, commands=['Завантажити товар'])
    dp.register_message_handler(load_item, Text(equals=['Завантажити товар'], ignore_case="/"))
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(load_articul, state=FSMAdmin.articul)
    dp.register_message_handler(load_quantity, state=FSMAdmin.quantity)
    dp.register_message_handler(log_out, state="*", commands='exit')
    dp.register_message_handler(log_out, Text(equals='exit', ignore_case=True), state="*")
