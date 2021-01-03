import csv

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher


BOT_TOKEN = 'token'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


'''

people
record_id, name_of_user, tg_id, timestamp, debt_amount


payments
record_id, name_of_user, tg_id, timestamp, payment_amount

'''


@dp.message_handler(commands=["start"])
async def start_command(msg: types.Message):
    start_msg = '''
Bot Help:
Send *<payment_amount>* to search for user info'''
    await msg.answer(start_msg, parse_mode="markdown")


@dp.message_handler()
async def handle_message(msg: types.Message):
    if msg.text.isdigit():
        # TODO worker_func(msg.text)
        await msg.answer(
            'Thanks for payment.',
            parse_mode="markdown"
        )
    else:
        await msg.answer(
            'Not found.',
            parse_mode="markdown"
        )

if __name__ == "__main__":
    try:
        executor.start_polling(dp)
    except Exception as e:
        print('Error while polling: {}'.format(e))


# with open('people.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         for e in row:
#             print(e)
