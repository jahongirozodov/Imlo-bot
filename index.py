import logging

from aiogram import Bot, Dispatcher, executor, types
from func import checkword
from transliterate import to_latin,to_cyrillic

API_TOKEN = '5974051714:AAHSvTJBqFZfbFhe1MQC5tCG_DmVwDL-KoY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu Aleykum botimizga hush kelibsiz!!!")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Botdan foydalanish uchun so'z yuboring!!!")



@dp.message_handler()
async def Checkimlo(message: types.Message):
    word = to_cyrillic(message.text)

    result = checkword(word)


    if result['avaible']:
        response = f"✅ {word.capitalize()}\n"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['word']:
            response += f"✅ {text.capitalize()}\n"
    await message.reply(to_latin(response))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

