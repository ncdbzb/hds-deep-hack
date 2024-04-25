from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


big_button_1 = InlineKeyboardButton(
    text='Кнопка',
    callback_data='big_button_1_pressed'
)

keyboard = InlineKeyboardBuilder()

keyboard.row(big_button_1, width=1)
