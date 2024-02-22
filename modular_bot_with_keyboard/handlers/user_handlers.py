from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from lexicon.lexicon import BASIC_ANSWERS
from keyboards.keyboard import keyboard


router = Router()


@router.message(CommandStart())
async def process_comand_start(message: Message):
    await message.answer(
        text=BASIC_ANSWERS["/start"],
        reply_markup=keyboard
    )
