from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from dotenv import load_dotenv
import os
import uuid
from app.utils import process_csv

from app.logger import logger

load_dotenv()
app = FastAPI(title="Walmart Content Refiner API")

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Welcome to Walmart Content Refiner API!"}


@app.post("/refine")
async def refine_content(file: UploadFile = File(...)):
    """Upload a CSV → process → return downloadable output path."""
    try:
        input_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}_{file.filename}")
        output_path = os.path.join(OUTPUT_DIR, f"refined_{os.path.basename(input_path)}")
        logger.info(f"Output File path {output_path}")

        with open(input_path, "wb") as f:
            f.write(await file.read())
        logger.info("Starting processing CSV")
        result_path = process_csv(input_path, output_path)

        return FileResponse(result_path, filename=os.path.basename(result_path))

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

