from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from lexicon.lexicon_ru import LEXICON_RU
from services.demo import get_bottom_group_course, ABBREVIATION

# Создаем клавиатуру с кнопками Факультетов
faculty: InlineKeyboardMarkup = InlineKeyboardMarkup()

button_engineers: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['engineers'],
                                                              callback_data='engineers')
button_management: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['management'],
                                                               callback_data='management')

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
faculty.add(button_engineers, button_management)


# Создаем клавиатуру с кнопками Направления
direction: InlineKeyboardMarkup = InlineKeyboardMarkup()

button_arch: InlineKeyboardButton = InlineKeyboardButton(LEXICON_RU['arch'])
button_bild: InlineKeyboardButton = InlineKeyboardButton(LEXICON_RU['bild'])

# Располагаем кнопки в клавиатуре рядом друг с другом в одном ряду
direction.add(button_arch, button_bild)

# Создаем клавиатуру с кнопками Пяти курсов (архитектура)
course_arch: InlineKeyboardMarkup = InlineKeyboardMarkup()

button_course_1: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['course_1'], callback_data='course_1')
button_course_2: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['course_2'], callback_data='course_1')
button_course_3: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['course_3'], callback_data='course_1')
button_course_4: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['course_4'], callback_data='course_1')
button_course_5: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['course_5'], callback_data='course_1')

course_arch.add(button_course_1, button_course_2, button_course_3,
                button_course_4, button_course_5)


group: InlineKeyboardMarkup = InlineKeyboardMarkup()

list_button_name: list = get_bottom_group_course(ABBREVIATION['Строительство'], 3)
button_list = [InlineKeyboardButton(text=x, callback_data=x) for x in list_button_name]
group.add(*button_list)
