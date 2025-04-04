from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from bot.config.settings import TOKEN, WEBHOOK_URL
from bot.handlers.menu_handler import router as menu_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(menu_router)

async def set_commands():
    await bot.set_my_commands([
        BotCommand(command="start", description="Запустить бота"),
    ])

async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)
    await set_commands()

app = web.Application()
setup_application(app, dp, bot)
app.router.add_post("/webhook", SimpleRequestHandler(dp, bot).handle)

if __name__ == "__main__":
    web.run_app(app, port=8000)