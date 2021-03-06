import sqlite3 as sq

from TOKEN import DATA_BASE
from created_bot import bot


def sql_start():
    global base, cur
    base = sq.connect(DATA_BASE)
    cur = base.cursor()
    base.execute("""CREATE TABLE IF NOT EXISTS assortment(img,
                name TEXT, description TEXT, price TEXT, 
                quantity TEXT, articul TEXT PRIMARY KEY);""")
    base.commit()


async def sql_add_items(state):
    async with state.proxy() as data:
        cur.execute("""INSERT INTO assortment VALUES (?,?,?,?,?,?);""", tuple(data.values()))
        base.commit()


async def get_all_assortment(message):
    for ret in cur.execute("""SELECT * FROM assortment""").fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'{ret[1]}\n Описание: {ret[2]}\n Цена: {ret[3]}\n')
