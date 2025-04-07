# NDTC CONV API

Made in python using FastApi, Openpyxl, Weasyprint

## Installation
```
virtualenv venv
venv/Scripts/activate
pip install "fastapi[standard]"
pip install -r requirements
```
For weasyprint check docs [here](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation)

## Post installation
- Create keys.py file and put api keys in a set named API_KEYS
- Generate api keys using key_gen.py and put it in API_KEYS

Run the api
- Dev
```
fastapi dev main.py
```
- Prod
```
uvicorn main:app --host 0.0.0.0 --port 80
```


## Usage
- Converts JSON to XLSX

```
/json-to-xlsx/{method_id}?api_key=...
```

- Converts XLSX to JSON
```
/xlsx-to-json?api_key=....
```
- Converts HTML to PDF
```
/html-to-pdf/{method_id}?api_key=...
```

Test cases are written in tests.py

method_id = 1 for getting the data stream <br>
method_id = 2 for getting the url of the file <br>
*files are saved on the disk for 60sec*

## Task List
- [x] JSON to XLSX
- [X] XLSX to JSON
- [X] Test for JSON <-> XLSX
- [x] HTML to PDF
- [x] Test for HTML -> PDF
- [x] API key auth
- [ ] Add logger

