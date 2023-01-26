from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import group, faculty
from services.services import get_timetable


# Этот хэндлер срабатывает на команду /start
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=faculty)


# Этот хэндлер будет срабатывать на команду /help
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=faculty)


# Этот хэндлер срабатывает на Инженерную академию
async def process_engineers(message: Message):
    await message.answer(text=LEXICON_RU['engineers'], reply_markup=group)


# Этот хэндлер срабатывает на любую из игровых кнопок
async def process_game_button(message: Message):
    bot_choice = get_timetable()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} - {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)


async def get_time_tabl


# Функция для регистрации хэндлеров в диспетчере. Вызывается в исполняемом файле bot.py
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(process_help_command, commands='help')
    dp.register_message_handler(process_engineers, text=LEXICON_RU['engineers'])
