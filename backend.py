from fastapi import FastAPI, UploadFile, File
from process_dataset import ProcessDataset

app = FastAPI()

# uvicorn backend:app --reload

@app.get("/health")
def read_root():
    return {"health": "FastAPI Server running."}

@app.post("/process-file")
async def process_file(file: UploadFile = File(...)):
    try:
        process_ds = ProcessDataset(file.file, file.filename)
        columns = process_ds.columns()
        return {"columns": columns}
    except Exception as e:
        return {"error": str(e)}

    
