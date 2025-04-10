import os
from fastapi import FastAPI, HTTPException, Request, File, UploadFile, Depends, Query
from fastapi.responses import FileResponse, StreamingResponse
import utils
from dotenv import load_dotenv

load_dotenv()

KEY = os.getenv("API_KEY")

def verify_api_key(api_key: str = Query(...)):
    if api_key != KEY:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")


app = FastAPI(dependencies=[Depends(verify_api_key)])


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
        download_url = f"{request.base_url}download/{data}?api_key={KEY}"
        return {"url": download_url}

@app.get("/download/{token}")
async def download_file(token: str):
    path = utils.token_map.get(token)
    fname = os.path.basename(path)
    if not path or not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found or expired")

    return FileResponse(
        path,
        filename=fname,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

@app.post("/xlsx-to-json")
async def xlsx_to_json(file: UploadFile = File(...)):
    contents = await file.read()
    json_data = utils.xlsx_to_json(contents)

    return json_data

@app.post("/html-to-pdf/{method_id}")
async def html_to_pdf(method_id: int,request: Request, file: UploadFile = File(...)):
    html_content = await file.read()
    pdf_data = utils.html_to_pdf(html_content, method_id)

    if method_id not in [1,2]:
        return {"error": "/<method_id>/ must be 1 or 2"}

    if method_id == 1:
        return StreamingResponse(
            pdf_data,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=result.pdf"}
        )
    elif method_id == 2:
        download_url = f"{request.base_url}download/{pdf_data}?api_key={KEY}"
        return {"url": download_url}