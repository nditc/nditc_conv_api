from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import utils

app = FastAPI()


@app.get("/")
def read_root():
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