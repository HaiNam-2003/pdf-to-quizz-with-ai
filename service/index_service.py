from service.model_service import ModelService
from service.pdf_service import PdfService
# from model_service import ModelService
# from pdf_service import PdfService
import shutil
import os

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
    
# print(indexService().result("chovy"))