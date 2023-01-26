from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

# Создаем клавиатуру с кнопками Факультетов
faculty: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                   resize_keyboard=True)

button_engineers: KeyboardButton = KeyboardButton(LEXICON_RU['engineers'])
button_management: KeyboardButton = KeyboardButton(LEXICON_RU['management'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
faculty.add(button_engineers, button_management)


# Создаем клавиатуру с кнопками Группы
group: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                 resize_keyboard=True)

button_arch: KeyboardButton = KeyboardButton(LEXICON_RU['arch'])
button_bild: KeyboardButton = KeyboardButton(LEXICON_RU['bild'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
group.add(button_arch, button_bild)
