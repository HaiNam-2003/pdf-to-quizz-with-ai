from fastapi import APIRouter,UploadFile,File
from fastapi.responses import JSONResponse
from service.index_service import indexService
from util.output_parse import Parse
import shutil

router = APIRouter()



@router.get("/")
async def create_student(name):
    index_service = indexService()
    response = index_service.result(fileName=name)
    return response

@router.post("/pdf")
async def edit_pdf_endpoint(input_pdf: UploadFile = File(...)):
    index_service = indexService()
    text = index_service.result(input_pdf=input_pdf)
    parse = Parse()
    response = parse.parse_questions(text=text)
    print(response)
    return {"status" : "200","data" : response }