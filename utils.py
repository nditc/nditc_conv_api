from openpyxl import Workbook, load_workbook


json_test_data = [
    {
        "name":"Fren",
        "id": 1
    },
    {
        "name":"Eren",
        "id": 2
    },
    {
        "name":"Kira",
        "id": 3
    },
    {
        "name":"Kira",
        "id": 3
    }
]

def json_to_xlsx(json_data):
    all_keys = set()
    for item in json_data:
        all_keys.update(item.keys())
    headers = all_keys

    wb = Workbook()
    ws = wb.active

    ws.append(headers)

    for item in json_data:
        row = [item.get(key, "") for key in headers]
        ws.append(row)
    wb.save("output.xlsx")

def xlsx_to_json(xlsx_filepath):
    wb = load_workbook(xlsx_filepath)
    ws = wb.active

    headers = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1))]

    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        item = {headers[i]: row[i] for i in range(len(headers))}
        data.append(item)
    return data

if __name__ == "__main__":
    # json_to_xlsx(json_test_data)
    data = xlsx_to_json("output.xlsx")
    print(data)