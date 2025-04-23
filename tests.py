import requests

# base_url = "http://127.0.0.1:5000"
base_url = "https://rown.pythonanywhere.com"

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

data = [{
        "id": 1092,
        "userName": "raf_l_coder@1741970342077",
        "mode": "par",
        "iat": 1744381273,
        "exp": 1746973273,
        "fullName": "Raf_L_coder",
        "image": "https://res.cloudinary.com/dxvw2ccph/image/upload/v1742909061/init/uploads/participants/raf_l_coder%25401742909053633.jpg",
        "email": "rafsanamin2020@gmail.com",
        "phone": "01713753930",
        "institute": "Notre Dame College",
        "className": "12",
        "address": "Uttara, Dhaka",
        "fb": "https://www.facebook.com/profile.php?id=100082305411559",
        "qrCode": "raf_l_coderm890608j",
        "isAppliedCA": True,
        "isCA": True,
        "caData": {
            "points": 0,
            "code": "m8oibxe0"
        },
        "clientEvents": [
            "snack",
            "lunch",
            "soloPass",
            "webPageDesigningDevelopment",
            "spotNGo"
        ]
    }, {
        "id": 1092,
        "userName": "raf_l_coder@1741970342077",
        "mode": "par",
        "iat": 1744381273,
        "exp": 1746973273,
        "fullName": "Raf_L_coder",
        "image": "https://res.cloudinary.com/dxvw2ccph/image/upload/v1742909061/init/uploads/participants/raf_l_coder%25401742909053633.jpg",
        "email": "rafsanamin2020@gmail.com",
        "phone": "01713753930",
        "institute": "Notre Dame College",
        "className": "12",
        "address": "Uttara, Dhaka",
        "fb": "https://www.facebook.com/profile.php?id=100082305411559",
        "qrCode": "raf_l_coderm890608j",
        "isAppliedCA": True,
        "isCA": True,
        "caData": {
            "points": 0,
            "code": "m8oibxe0"
        },
        "clientEvents": [
            "snack",
            "lunch",
            "soloPass",
            "webPageDesigningDevelopment",
            "spotNGo"
        ]
    }]


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

    files = {'file': open('example.html', 'r')}
    response = requests.post(url, files=files)
    
    print("Status code:", response.status_code)
    print("Response:", response.text)


if __name__ == "__main__":
    # test_xlsx_to_json()
    test_json_to_xlsx()
    # test_html_to_pdf()
