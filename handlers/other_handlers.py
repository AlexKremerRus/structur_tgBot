from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

router=Router()

# этот хэндлер работает на все кроме хелпа и старта
@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer(text=LEXICON_RU['no_echo'])