import os
import threading
from fastapi import FastAPI, HTTPException, Request, File, UploadFile
from fastapi.responses import FileResponse, StreamingResponse
import utils

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/json-to-xlsx/{method_id}")
async def json_to_xlsx(request: Request, method_id: int):
    data = await request.json()

    if not isinstance(data, list):
        return {"error": "JSON must be a list of objects"}
    elif method_id not in [1, 2]:
        return {"error": "/<method_id>/ must be 1 or 2"}

    
    data = utils.json_to_xlsx(data, method_id)


    if method_id == 1:
        return StreamingResponse(
            data,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=result.xlsx"}
        )
    elif method_id == 2:
        download_url = f"{request.base_url}download/{data}"
        return {"url": download_url}

@app.get("/download/{token}")
async def download_file(token: str):
    path = utils.token_map.get(token)
    if not path or not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found or expired")

    return FileResponse(
        path,
        filename=f"{token}.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@app.post("/xlsx-to-json")
async def xlsx_to_json(file: UploadFile = File(...)):
    contents = await file.read()
    json_data = utils.xlsx_to_json(contents)

    return json_data