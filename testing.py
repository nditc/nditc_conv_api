import requests

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
    url = "http://127.0.0.1:8000/json-to-xlsx/"

    response = requests.post(url, json=data)

    print("Status code:", response.status_code)
    print("Response:", response.text)


