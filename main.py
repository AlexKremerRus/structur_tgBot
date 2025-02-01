import asyncio

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers


async def main() -> None:
    config: Config=load_config()

    bot = Bot(token = config.tg_bot.token)
    
    dp = Dispatcher()

    # регистрируем Роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # пропускаем накопившиеся апдейты и делаем запуск

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())

