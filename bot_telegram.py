from aiogram.utils import executor
from aiogram.utils.exceptions import NetworkError
from aiohttp import ClientConnectorError
from created_bot import dp
from loguru import logger
from Catch_message import admin, client, other_part
from data_base import sqlite_db


logger.add('debug.log', format='{time} {level} {message}', level='DEBUG',
           rotation='10 KB', compression='zip')


async def on_startup(args):
    logger.info('Бот вышел онлайн')
    sqlite_db.sql_start()
    logger.info('БД подключена')


client.register_hendlers(dp)
admin.register_handlrs_admin(dp)
other_part.register_hendlers_others(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

