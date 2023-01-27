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


def get_cells_group(worksheet, index_group):
    courses = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    cells_group = [cell for cell in next(
        worksheet.iter_rows(min_row=5, min_col=5, max_row=5, max_col=worksheet.max_column))]

    print(cells_group)

def get_group():
    for group in cells_group:
        group = group.value
        if re.match(fr'{index_group}', group):
            course_group = get_course_number(group)
            courses[course_group].append(group)
    print(courses)

data_path = join('.', 'demo_timetable.xlsx')
data_path_abs = abspath(data_path)

wb = load_workbook(filename=data_path_abs, read_only=True, data_only=True)
wsn = wb.sheetnames
name_first_sheet = str(wsn[0])
ws = wb[name_first_sheet]
arch_groups = get_group(ws, ABBREVIATION['Архитектура'])
print(arch_groups)
# cail = arch_groups[3][0]
# print(type(cail))

