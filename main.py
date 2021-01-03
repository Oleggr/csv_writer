import csv

from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher


BOT_TOKEN = '944547365:AAH67D-oXzAtRXdYX5SsZtBFq_m_rOMxaWA'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


'''

people
record_id, name_of_user, tg_id, timestamp, debt_amount


payments
record_id, name_of_user, tg_id, timestamp, payment_amount

'''

with open('people.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            print(e)

try:
    executor.start_polling(dp)
except Exception as e:
    print('Error while polling: {}'.format(e))