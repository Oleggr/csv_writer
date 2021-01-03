import csv, re

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from csvWriter import csvWriter


admins = ['admin_id', 'second_admin_id']
BOT_TOKEN = 'token'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

writer = csvWriter()


@dp.message_handler(commands=["start"])
async def start_command(msg: types.Message):
    start_msg = '''
Bot Help:
Send *<payment_amount>* to insert your new payment'''
    await msg.answer(start_msg, parse_mode="markdown")

@dp.message_handler(commands=["dept"])
async def start_command(msg: types.Message):
    patt = r'(?P<name>[\wА-Яа-я]+)\s*,\s*(?P<payment>\d+)'
    values = re.search(patt, msg.text)
    if patt is not None:
        name, paymant = values.group('name'), values.group('payment')
        # TODO fucntion to write values
        await msg.answer('Success')
    else:
        await msg.answer('Nothing to write')

@dp.message_handler()
async def handle_message(msg: types.Message):
    if msg.text.isdigit():
        writer.writePayment(
            msg.from_user.full_name,
            msg.from_user.id,
            int(msg.text)
        )
        await msg.answer(
            'Thanks for your *%s* payment.' % writer.getPaymentsCount(msg.from_user.id),
            parse_mode="markdown"
        )
    else:
        await msg.answer(
            'Wrong input. Try another number',
            parse_mode="markdown"
        )

if __name__ == "__main__":
    try:
        executor.start_polling(dp)
    except Exception as e:
        print('Error while polling: {}'.format(e))
