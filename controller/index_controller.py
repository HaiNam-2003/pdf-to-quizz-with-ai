from fastapi import APIRouter,UploadFile,File
from fastapi.responses import JSONResponse
from service.index_service import indexService
from util.output_parse import Parse
import shutil
from typing import List, Dict
from model.question_model import QuizData

router = APIRouter()



@router.get("/pdf")
async def create_student():
    return "hellos"

from fastapi import HTTPException

@router.post("/pdf")
async def edit_pdf_endpoint(input_pdf: UploadFile = File(...)):
    try:
        index_service = indexService()
        text = index_service.result(input_pdf=input_pdf)
        parse = Parse()
        response = parse.parse_questions(text=text)
        return {"data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))
    
@router.post("/save_quiz")
async def process_quiz_data(quiz_data: QuizData):
    try:
        print(quiz_data)
        await indexService().saveQuiz(quiz=quiz_data.data)
        return {"message": "Quiz data received successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error: " + str(e))

@router.get("/test")
async def test():
    result = await indexService().read_quiz(1)
    return result