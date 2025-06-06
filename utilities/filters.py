"""Custom filters."""

from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class RoleFilter(BoundFilter):
    def __init__(self, role: str):
        self.role = role

    async def check(self, message: types.Message) -> bool:
        # Placeholder for role check from DB
        return False
