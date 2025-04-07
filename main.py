from typing import Union
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import StreamingResponse
import utils

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/json-to-xlsx")
async def json_to_xlsx(request: Request):
    data = await request.json()

    if not isinstance(data, list):
        return {"error": "JSON must be a list of objects"}
    
    data_stream = utils.json_to_xlsx(data)

    return StreamingResponse(
        data_stream,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=result.xlsx"}
    )

@app.post("/xlsx-to-json")
async def xlsx_to_json(file: UploadFile = File(...)):
    contents = await file.read()
    json_data = utils.xlsx_to_json(contents)

    return json_data