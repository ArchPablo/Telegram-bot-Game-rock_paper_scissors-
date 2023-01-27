from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import faculty, direction, course_arch, group
from services.services import get_timetable


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=faculty)


# Этот хэндлер будет срабатывать на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=faculty)


# Этот хэндлер срабатывает на Инженерную академию
async def process_engineers(message: Message):
    await message.answer(text=LEXICON_RU['engineers'], reply_markup=direction)


async def process_direction_arch(message: Message):
    await message.answer(text=LEXICON_RU['arch'], reply_markup=course_arch)


async def process_group(message: Message):
    await message.answer(text='3', reply_markup=group)


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_engineers, text=LEXICON_RU['engineers'])
    dp.register_message_handler(process_direction_arch, text=LEXICON_RU['arch'])
    dp.register_message_handler(process_group, text=LEXICON_RU['course_3'])
