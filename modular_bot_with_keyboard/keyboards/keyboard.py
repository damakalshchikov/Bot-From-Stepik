from aiogram.types import ReplyKeyboardMarkup
from buttons.buttons_for_keyboard import button_1, button_2


keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],
    resize_keyboard=True,
    one_time_keyboard=True
)
