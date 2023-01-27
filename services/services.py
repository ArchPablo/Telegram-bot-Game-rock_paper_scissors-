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


