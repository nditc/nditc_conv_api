import requests

API_KEY = ""

data = [
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

def test_json_to_xlsx():
    url = f"http://127.0.0.1:8000/json-to-xlsx?api_key={API_KEY}"

    response = requests.post(url, json=data)

    print("Status code:", response.status_code)
    print("Response:", response.text)


def test_xlsx_to_json():
    url = f"http://localhost:8000/xlsx-to-json/2?api_key={API_KEY}"
    files = {'file': open('example.xlsx', 'rb')}
    response = requests.post(url, files=files)

    print(response.json())

def test_html_to_pdf():
    url = f"http://127.0.0.1:8000/html-to-pdf/2?api_key={API_KEY}"

    files = {'file': open('example.html', 'r')}
    response = requests.post(url, files=files)
    
    print("Status code:", response.status_code)
    print("Response:", response.text)


if __name__ == "__main__":
    test_xlsx_to_json()
    # test_json_to_xlsx()
    # test_html_to_pdf()