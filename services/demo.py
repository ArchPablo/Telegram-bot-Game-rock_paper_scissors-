import datetime
import re
import math

from openpyxl import load_workbook, Workbook
from os.path import join, abspath

ABBREVIATION = {'Архитектура': 'ИАРбд'}


class NotAllData(Exception):
    pass


# Функция высчитывает на каком курсе учится группа без учета високосного года
def get_course_number(name_group: str) -> int:
    year_admission = int(f'20{name_group[9:]}')
    start_admission = datetime.date(year_admission, 8, 1)
    study_days = (datetime.date.today()-start_admission).days
    course = math.ceil(study_days / 365)
    return course


def get_cells_group(worksheet):
    cells = [cell for cell in next(
        worksheet.iter_rows(min_row=5, min_col=5, max_row=5, max_col=worksheet.max_column))]
    return cells


def get_courses_group(cells, index_group):
    courses = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for group in cells:
        group = group.value
        if re.match(fr'{index_group}', group):
            course_group = get_course_number(group)
            courses[course_group].append(group)
    return courses


def get_timetable(sheet, column_group):
    timetable_week = {'Понедельник': [], 'Вторник': [], 'Среда': [],
                      'Четверг': [], 'Пятница': [], 'Суббота': []}
    time_table = [cell.value for cell in next(
        sheet.iter_cols(min_row=6, min_col=column_group, max_row=sheet.max_row, max_col=column_group))]
    day = 0
    for timetable_day in timetable_week:
        for lesson in range(day, day+8):
            timetable_week[timetable_day].append(time_table[lesson])
        day += 8
    return timetable_week


data_path = join('.', 'demo_timetable.xlsx')
data_path_abs = abspath(data_path)

wb = load_workbook(filename=data_path_abs,  data_only=True)
wsn = wb.sheetnames
name_first_sheet = str(wsn[0])
ws = wb[name_first_sheet]
cells_group = get_cells_group(ws)
arch_groups = get_courses_group(cells_group, ABBREVIATION['Архитектура'])






    # for item in time_table:

tt = get_timetable(ws, 5)
print(tt)
for i in tt:
    print(i, end=f'________\n')
    for j in tt[i]:
        print(j)
wb.close()
# cail = arch_groups[3][0]
# print(type(cail))

