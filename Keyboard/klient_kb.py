from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('В наявності')
b3 = KeyboardButton('Доставка')
b4 = KeyboardButton('Кошик')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.row(b1).row(b3, b4)








