from aiogram import Router
from aiogram.types import Message
from filters.admin_filters import IsAdminFilter
from lexicon.lexicon import ADMIN_LEXICON
from bot import admin_ids


router = Router()


@router.message(IsAdminFilter(admin_ids=admin_ids))
async def process_is_admin(message: Message):
    await message.answer(text=ADMIN_LEXICON["admin"])
