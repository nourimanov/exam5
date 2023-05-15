import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
TOKEN = "5601282041:AAG2pU-4iPyiq3168do8JXI1ALkiXW8skX8"
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
@dp.message_handler()
async def start(message: types.Message):
    count = sum(1 for msg in message.text if msg in ['a', 'o', 'u', 'i', 'e'])
    if count >= 5:
        await bot.delete_message(message.chat.id, message.message_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
