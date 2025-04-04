from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
import asyncio
from bot.config.settings import TOKEN, WEBHOOK_URL

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def set_commands():
    await bot.set_my_commands([
        BotCommand(command="start", description="Запустить бота"),
    ])

async def main():
    from bot.handlers.menu_handler import router as menu_router  # Переместили импорт внутрь функции
    dp.include_router(menu_router)

    await bot.set_webhook(WEBHOOK_URL)
    await set_commands()

    app = web.Application()
    setup_application(app, dp, bot)
    app.router.add_post("/webhook", SimpleRequestHandler(dp, bot).handle)

    return app

if __name__ == "__main__":
    asyncio.run(main())