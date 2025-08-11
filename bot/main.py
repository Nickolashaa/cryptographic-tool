import core.config as cfg
from aiogram import Bot, Dispatcher
from .router import get_routers


async def main():
    bot = Bot(token=cfg.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(get_routers())
    print("Bot Started.")
    await dp.start_polling(bot)
