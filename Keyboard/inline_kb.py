from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types, Dispatcher
from created_bot import bot


inline_markup = InlineKeyboardMarkup()
men_button = InlineKeyboardButton('Шкарпетки Чоловічі', callback_data='men_button')
women_button = InlineKeyboardButton('Шкарпетки Жіночі', callback_data='women_button')
inline_markup.add(men_button, women_button)


async def men_button(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, 'Кнопку нажали')


def register_handlers_inline(dp: Dispatcher):
    @dp.register_message_handler(men_button, lambda c: c.data == 'men_button')







