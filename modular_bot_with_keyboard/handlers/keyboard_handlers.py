from aiogram import Router
from aiogram.types import Message
from filters.keyboard_filters import IsDogFilter, IsCucumberFilter
from lexicon.lexicon import LEXICON


router = Router()


@router.message(IsDogFilter())
async def process_dog_answer(message: Message):
    await message.answer(text=LEXICON["is_dog"])


@router.message(IsCucumberFilter())
async def process_cucumber_answer(message: Message):
    await message.answer(text=LEXICON["is_cucumber"])
