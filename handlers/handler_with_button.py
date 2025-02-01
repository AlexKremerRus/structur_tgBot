from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

router = Router()

# Создаем кнопки
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')

# Создаем клавиатуру для кнопок

keyboard = ReplyKeyboardMarkup(keyboard=[button_1, button_2])


