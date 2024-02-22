from aiogram.filters import BaseFilter
from aiogram.types import Message
from lexicon.lexicon import TEXT_FOR_BUTTONS


class IsDogFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text == TEXT_FOR_BUTTONS["button_1"]


class IsCucumberFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.text == TEXT_FOR_BUTTONS["button_2"]
