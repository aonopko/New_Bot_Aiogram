from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_markup = InlineKeyboardMarkup()
christmas_socks_button = InlineKeyboardButton('Дитячі',
                                              url='https://www.instagram.com/stories/highlights/17901165119334978/')
warm_socks_button = InlineKeyboardButton('Чоловічі',
                                         url='https://www.instagram.com/stories/highlights/17976430339464564/')

inline_markup.add(christmas_socks_button, warm_socks_button)
