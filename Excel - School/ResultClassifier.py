from openpyxl import load_workbook
from openpyxl import Workbook

wb = load_workbook(filename=str(input()))
ws = wb.worksheets[0].title
ws = wb[ws]
wr = Workbook()
result = wr.create_sheet(title="Result")

subjects = {}
starting_column = "D"
while ws[starting_column + '5'].value:
    subjects[ws[starting_column + '5'].value] = {"column": starting_column, "distribution": [0 for _ in range(10)],
                                                 "passing": 0, "failing": 0}
    starting_column = chr(ord(starting_column) + 1)

for i in range(10):
    result[f'{chr(ord("A") + i + 1)}' + '1'] = f'{10 * i} to {10 * (i + 1)}'
result[f'{chr(ord("A") + 11)}' + "1"] = "Pas"
result[f'{chr(ord("A") + 12)}' + "1"] = "Fail"

for key, value in subjects.items():
    sr = 9
    try:
        max_marks = int(str(ws[value["column"] + f'{sr - 1}'].value)[1:])
    except ValueError:
        continue
    scale = 100 / max_marks
    while ws[value["column"] + f'{sr}'].value or ws[value["column"] + f'{sr}'].value == 0:
        try:
            marks = float(ws[value["column"] + f'{sr}'].value) * scale
        except ValueError:
            if ws[value["column"] + f'{sr}'].value == '---':
                sr += 2
                continue
            marks = 0
        if marks >= 33:
            value["passing"] += 1
        else:
            value["failing"] += 1
        value["distribution"][min(int(marks / 10), 9)] += 1
        sr += 2

    result["A" + f'{ord(value["column"]) - ord("A")}'] = key
    for i in range(len(value["distribution"])):
        result[f'{chr(ord("A") + 1 + i)}' + f'{ord(value["column"]) - ord("A")}'] = value["distribution"][i]
    result[f'{chr(ord("A") + 11)}' + f'{ord(value["column"]) - ord("A")}'] = value["passing"]
    result[f'{chr(ord("A") + 12)}' + f'{ord(value["column"]) - ord("A")}'] = value["failing"]

wr.save(filename='result.xlsx')
