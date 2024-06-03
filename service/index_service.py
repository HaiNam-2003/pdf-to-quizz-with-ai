from service.model_service import ModelService
from service.pdf_service import PdfService
# from model_service import ModelService
# from pdf_service import PdfService
import shutil
import os
import json
import random
from repository.connect import save_quiz_to_database, execute_query

class indexService():
    def __init__(self):
        pass
    def result(self,input_pdf):
        modelService = ModelService()
        pdfService = PdfService()
        temp_pdf_path = f"/Users/mac/Documents/Final Project/app/data/temp/{input_pdf.filename}"
        with open(temp_pdf_path, "wb") as temp_pdf:
                shutil.copyfileobj(input_pdf.file, temp_pdf)
        fileVectorStore = pdfService.create_db_from_files(fileName=input_pdf.filename)
        response = modelService.respone(file_data_path=fileVectorStore)
        os.remove(temp_pdf_path)
        shutil.rmtree(fileVectorStore)
        return response["result"]     
    async def saveQuiz(self, quiz):   
        while True:
            # Tạo một số ngẫu nhiên
            random_number = random.randint(1, 10000)    # Import 'random' để sử dụng
            file_path = f"/Users/mac/Documents/Final Project/app/data/pdf/{random_number}.json"
            # Kiểm tra xem tệp có tồn tại không
            if not os.path.exists(file_path):
                # Nếu tệp không tồn tại, ghi dữ liệu vào tệp và thoát khỏi vòng lặp
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump([quiz_item.dict() for quiz_item in quiz], file, indent=4, ensure_ascii=False)
                    result = await save_quiz_to_database(random_number)
                    print(result)
                break
        return "success"
    async def read_quiz(self,user_id):
        result = await execute_query(user_id)
        list_quiz = []
        for index, value in enumerate(result):
            result2 = self.get_file_json(value)
            list_quiz.append(result2)
        return list_quiz        
    def get_file_json(self,file_name):
        file_path = f"/Users/mac/Documents/Final Project/app/data/pdf/{file_name}.json"
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data
# print(indexService().result("chovy"))