"""Helper functions for BotFlatMatcher."""

from aiogram import types


async def send_welcome(message: types.Message):
    await message.answer("Welcome to BotFlatMatcher!")
