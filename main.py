import os
from fastapi import FastAPI, File, UploadFile, Request
from indexing import index_documents, search_by_index

app = FastAPI()

SUPPORTED_EXTENSIONS = ["pdf", "docx"]
UPLOAD_FOLDER = "documents"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post('/load-documents/')
async def load_documents(files: list[UploadFile] = File(...)):
    uploaded_files = []
    not_supported_files = []
    uploaded_file_paths = []
        
    for file in files:
        if file.filename.split(".")[-1] not in SUPPORTED_EXTENSIONS:
            not_supported_files.append(file.filename)
        else:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            with open(file_path, "wb") as f:
                f.write(await file.read())
            uploaded_files.append(file.filename)
            uploaded_file_paths.append(file_path)
            
    await index_documents(uploaded_file_paths)

    return {
        "message": "Documents were loaded.",
        "loaded_files": uploaded_files,
        "not_supported_files": not_supported_files
    }

@app.post('/search_documents/')
async def search_documents(request: Request):
    body = await request.json()
    return  await search_by_index(body)
   