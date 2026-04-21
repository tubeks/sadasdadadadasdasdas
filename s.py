import asyncio
from aiogram import Bot

TOKEN = "8724082151:AAGa7ch10KQ-ckKppLO9rgaB4AWY6OJVrmU"

async def test():
    bot = Bot(token=TOKEN)
    try:
        me = await bot.get_me()
        print(f"✅ Подключено! Бот: {me.username}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        await bot.session.close()

asyncio.run(test())