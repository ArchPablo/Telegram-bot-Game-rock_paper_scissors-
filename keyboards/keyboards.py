from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU
from services.demo import get_bottom_group_course, ABBREVIATION

# Создаем клавиатуру с кнопками Факультетов
faculty: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                   resize_keyboard=True)

button_engineers: KeyboardButton = KeyboardButton(LEXICON_RU['engineers'])
button_management: KeyboardButton = KeyboardButton(LEXICON_RU['management'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
faculty.add(button_engineers, button_management)


# Создаем клавиатуру с кнопками Направления
direction: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                     resize_keyboard=True)

button_arch: KeyboardButton = KeyboardButton(LEXICON_RU['arch'])
button_bild: KeyboardButton = KeyboardButton(LEXICON_RU['bild'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
direction.add(button_arch, button_bild)

# Создаем клавиатуру с кнопками Пяти курсов (архитектура)
course_arch: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                       resize_keyboard=True)

button_course_1: KeyboardButton = KeyboardButton(LEXICON_RU['course_1'])
button_course_2: KeyboardButton = KeyboardButton(LEXICON_RU['course_2'])
button_course_3: KeyboardButton = KeyboardButton(LEXICON_RU['course_3'])
button_course_4: KeyboardButton = KeyboardButton(LEXICON_RU['course_4'])
button_course_5: KeyboardButton = KeyboardButton(LEXICON_RU['course_5'])

course_arch.add(button_course_1, button_course_2, button_course_3,
                button_course_4, button_course_5)


group: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                 resize_keyboard=True)

list_button_name: list = get_bottom_group_course(ABBREVIATION['Строительство'], 3)
button_list = [KeyboardButton(text=x) for x in list_button_name]
group.add(*button_list)



