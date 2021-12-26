
from TOKEN import TOKEN
from aiogram import Bot
from aiogram.dispatcher import Dispatcher      # Класс позволяет реагировать на события в чате
from aiogram.contrib.fsm_storage.memory import MemoryStorage   # класс позволяет хранить данніе в ОЗУ


storage = MemoryStorage()

bot = Bot(token= TOKEN)
dp = Dispatcher(bot, storage=storage)






