import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import (
    admin_handlers, keyboard_handlers,
    user_handlers, other_handlers
    )


config: Config = load_config()
token: str = config.tg_bot.token
admin_ids: list[int] = config.tg_bot.admin_ids


async def main(bot_token) -> None:
    bot: Bot = Bot(token=bot_token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(keyboard_handlers.router)
    dp.include_router(admin_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main(bot_token=token))
