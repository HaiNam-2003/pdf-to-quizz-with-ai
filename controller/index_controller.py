from fastapi import APIRouter

from service.test.test2 import test
from service.test.util import parse_quiz_text
from service.index_service import indexService

router = APIRouter()

@router.get("/")
async def create_student(name):
    index_service = indexService()
    response = index_service.result(fileName=name)
    return response
