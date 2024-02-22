from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import BASIC_ANSWERS


router = Router()


@router.message()
async def process_everything(message: Message):
    await message.answer(text=BASIC_ANSWERS["everything"])
