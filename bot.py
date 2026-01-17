import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("8543772425:AAH-qom25IrEhgX8QEK_g-26KwuWc6I26BY")
ADMIN_ID = 1378166283

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 Здравствуйте!\n\n"
        "Онлайн-запись в барбершоп 💈\n\n"
        "Отправьте одним сообщением:\n"
        "• Имя\n"
        "• Дата\n"
        "• Время"
    )

@dp.message()
async def handle_message(message: types.Message):
    text = (
        "📩 Новая заявка:\n\n"
        f"👤 Имя: {message.from_user.full_name}\n"
        f"📝 Текст: {message.text}\n"
        f"🆔 ID: {message.from_user.id}"
    )
    await bot.send_message(ADMIN_ID, text)
    await message.answer("✅ Заявка отправлена!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
