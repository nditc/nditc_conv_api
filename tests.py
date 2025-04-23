import requests


API_KEY = "abcd"
base_url = "http://127.0.0.1:5000"
# base_url = "https://rown.pythonanywhere.com"

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
    url = f"{base_url}/json-to-xlsx/2?api_key={API_KEY}"

    response = requests.post(url, json=data)

    print("Status code:", response.status_code)
    print("Response:", response.text)


def test_xlsx_to_json():
    url = f"{base_url}/xlsx-to-json?api_key={API_KEY}"
    files = {'file': open('example.xlsx', 'rb')}
    response = requests.post(url, files=files)

    print(response.json())

def test_html_to_pdf():
    url = f"{base_url}/html-to-pdf/2?api_key={API_KEY}"

    with open('example.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    headers = {'Content-Type': 'text/html'}
    response = requests.post(url, data=html_content, headers=headers)
    
    print("Status code:", response.status_code)
    print("Response:", response.text)


if __name__ == "__main__":
    # test_xlsx_to_json()
    # test_json_to_xlsx()
    test_html_to_pdf()
