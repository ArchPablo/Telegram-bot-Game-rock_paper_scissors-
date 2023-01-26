import random
import pandas as pd

from lexicon.lexicon_ru import LEXICON_RU


def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key

def get_timetable_ex(user_choice: str, bot_choice: str) -> str:
    user_choice: str = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'


def get_timetable(user_choice: str) -> str:
    user_choice: str = _normalize_user_answer(user_choice)
    if user_choice == LEXICON_RU['engineers']:
        return LEXICON_RU['engineers']
    elif user_choice == LEXICON_RU['management']:
        return 'ok_1'


# Load the xlsx file
excel_data = pd.read_excel(f'.data_timetable.demo_timetable.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['Sales Date', 'Sales Person', 'Amount'])
# Print the content
print("The content of the file is:\n", data)
