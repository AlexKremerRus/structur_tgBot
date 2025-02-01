from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

router = Router()

# Хэндлер обрботки команды Старт
@router.message(CommandStart())
async def proccess_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'])

# Хэндлер обрботки команды хелпа
@router.message(Command(commands='help'))
async def proccess_help_command(message:Message):
    await message.answer(text=LEXICON_RU['/help'])


