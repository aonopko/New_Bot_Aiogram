from aiogram.utils import executor
from created_bot import dp
from Catch_message import admin, client, other_part
from data_base import sqlite_db
from Keyboard import inline_kb


async def on_startup(_):
    print('Бот вышел онлайн')
    sqlite_db.sql_start()


client.register_hendlers(dp)
admin.register_handlrs_admin(dp)
other_part.register_hendlers_others(dp)
inline_kbregister_handlers_inline(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

