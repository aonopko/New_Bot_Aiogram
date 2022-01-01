from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message
from aiogram import types, Dispatcher
from created_bot import dp
from created_bot import bot



inline_markup = InlineKeyboardMarkup()
christmas_socks_button = InlineKeyboardButton('Новорічні',
                                              url='https://www.instagram.com/stories/highlights/17914129988121812/')
warm_socks_button = InlineKeyboardButton('Теплі',
                                         url='https://www.instagram.com/stories/highlights/17920125134016005/')

inline_markup.add(christmas_socks_button, warm_socks_button)











