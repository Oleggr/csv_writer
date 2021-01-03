import csv

from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from csvWriter import csvWriter

#
# BOT_TOKEN = '944547365:AAH67D-oXzAtRXdYX5SsZtBFq_m_rOMxaWA'
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)


'''

people
name_of_user, tg_id, timestamp, debt_amount


payments
name_of_user, tg_id, timestamp, payment_amount

'''

writer = csvWriter()
writer.writePayment('vasya', 111, 120)
print(writer.getPaymentsCount(111))

#
# try:
#     executor.start_polling(dp)
# except Exception as e:
#     print('Error while polling: {}'.format(e))