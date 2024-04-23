from service.model_service import ModelService
from service.pdf_service import PdfService
# from model_service import ModelService
# from pdf_service import PdfService
class indexService():
    def __init__(self):
        pass
    def result(self,fileName):
        modelService = ModelService()
        pdfService = PdfService()
        fileVectorStore = pdfService.create_db_from_files(fileName=fileName)
        print("hello")
        response = modelService.respone(file_data_path=fileVectorStore)
        return response["result"]
    
# print(indexService().result("chovy"))