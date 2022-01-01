
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('\U0001f9E6  '+'В наявності')
b3 = KeyboardButton('\U0001f69A  '+'Доставка')
b4 = KeyboardButton('\U0001f440  '+'Весь асортимент')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1).row(b3, b4)








