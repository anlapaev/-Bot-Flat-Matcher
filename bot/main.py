import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, executor, types

from db.database import init_db

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"]) 
async def cmd_start(message: types.Message):
    await message.answer("Welcome to BotFlatMatcher! Use /help to see commands.")


@dp.message_handler(commands=["help"]) 
async def cmd_help(message: types.Message):
    await message.answer("This bot helps match renters and property owners.")


def main():
    init_db()
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
