from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram import Router, F

router = Router()

# Создаем кнопки
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')

# Создаем клавиатуру для кнопок

keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True,one_time_keyboard=True)


# Хэндлер обрботки команды Старт
@router.message(CommandStart())
async def proccess_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=keyboard)

# Хэндлер обрботки команды хелпа
@router.message(Command(commands='help'))
async def proccess_help_command(message:Message):
    await message.answer(text=LEXICON_RU['/help'])

@router.message(F.text == 'Собак 🦮' )
async def answer_dog(message: Message):
    await message.answer(text=LEXICON_RU['dog'])

@router.message(F.text == 'Огурцов 🥒' )
async def answer_cucumber(message: Message):
    await message.answer(text=LEXICON_RU['cucmber'])

