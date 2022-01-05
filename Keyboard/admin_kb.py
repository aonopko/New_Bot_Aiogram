from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

k1 = KeyboardButton('Завантажити товар')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.row(k1)
