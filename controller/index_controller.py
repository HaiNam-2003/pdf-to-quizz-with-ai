from fastapi import APIRouter,UploadFile,File

from service.test.test2 import test
from service.test.util import parse_quiz_text
from service.index_service import indexService
import shutil

router = APIRouter()

@router.get("/")
async def create_student(name):
    index_service = indexService()
    response = index_service.result(fileName=name)
    return response

@router.post("/pdf")
async def edit_pdf_endpoint(input_pdf: UploadFile = File(...)):
    # Lưu file PDF vào thư mục tạm
    temp_pdf_path = f"/path/to/temp/{input_pdf.filename}"
    with open(temp_pdf_path, "wb") as temp_pdf:
        shutil.copyfileobj(input_pdf.file, temp_pdf)