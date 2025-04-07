from io import BytesIO
import threading
import time
from openpyxl import Workbook, load_workbook
import base64
import os, uuid


token_map = {}
TEMP_DIR = "./files"
os.makedirs(TEMP_DIR, exist_ok=True)

def random_filename(byte_length=8):
    random_bytes = os.urandom(byte_length)
    return base64.urlsafe_b64encode(random_bytes).decode('utf-8').rstrip('=')

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

def schedule_cleanup(token: str, delay: int = 60):
    def cleanup():
        time.sleep(delay)
        path = token_map.pop(token, None)
        if path and os.path.exists(path):
            os.remove(path)
    threading.Thread(target=cleanup, daemon=True).start()

def json_to_xlsx(json_data, method_id):
    token = str(uuid.uuid4())
    filepath = os.path.join(TEMP_DIR, f"{token}.xlsx")

    all_keys = set()
    for item in json_data:
        all_keys.update(item.keys())
    headers = list(all_keys)

    wb = Workbook()
    ws = wb.active

    ws.append(headers)

    for item in json_data:
        row = [item.get(key, "") for key in headers]
        ws.append(row)

    if method_id == 1:
        stream = BytesIO()
        wb.save(stream)
        stream.seek(0)
        return stream
    elif method_id == 2:
        token_map[token] = filepath
        schedule_cleanup(token)
        wb.save(filepath)
        return token


def xlsx_to_json(xlsx_datastream):
    wb = load_workbook(BytesIO(xlsx_datastream))
    ws = wb.active

    headers = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1))]

    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        item = {headers[i]: row[i] for i in range(len(headers))}
        data.append(item)
    return data



if __name__ == "__main__":
    json_to_xlsx(json_test_data)
    # data = xlsx_to_json("output.xlsx")
    # print(data)