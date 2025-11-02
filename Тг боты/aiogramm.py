from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot("7022258546:AAG_bcOHkxwmZq-Og6ygY7hdu9vL7aFocCU")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(
        types.KeyboardButton(
            'Открыть веб страницу',
            web_app=WebAppInfo(url='https://www.google.com')
        )
    )
    await message.answer('Привет мой сладкий пирожочек :)', reply_markup=markup)



executor.start_polling(dp)
