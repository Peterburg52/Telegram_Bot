from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from bot.services.limiter import limiter

class RateLimiterMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        if not await limiter.acquire():
            await message.answer("Вы слишком часто отправляете запросы. Попробуйте позже.")
            raise CancelHandler()