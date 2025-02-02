from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram import Router, F
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()

#Создаем Бтлдел клавиатуры кнопок
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')
contact_btn = KeyboardButton(text='Отправить номер телфона',request_contact=True)
geo_btn = KeyboardButton(text='Отправить геолокацию', request_location=True)
poll_btn = KeyboardButton(text='Создание опроса', request_poll=KeyboardButtonPollType())

#Добавляем кнопки в билдер 
kb_builder.row(button_1,button_2,contact_btn,geo_btn,poll_btn , width=5)


# Создаем клавиатуру для кнопок Старое УЖЕ НЕАКТУАЛЬНО - ОСТАВЛЮ ДЛЯ ИСТОРИИ

# keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True,one_time_keyboard=True)

# Создаем объект клавиатуры

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

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

