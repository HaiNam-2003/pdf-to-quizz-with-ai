from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import GPT4AllEmbeddings
import random

class PdfService():
    def __init__(self):
        self.pdf_data_path = "/Users/mac/Documents/Final Project/app/data/temp"
        self.vector_db_path = "/Users/mac/Documents/Final Project/app/data/vectorstore"
    def create_db_from_files(self,fileName):
        # Khai bao loader de quet toan bo thu muc dataa
        loader = PyPDFLoader(f"{self.pdf_data_path}/{fileName}.pdf")    
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
        chunks = text_splitter.split_documents(documents)
        random_number = random.randint(1, 100)    # Embeding
        embedding_model = GPT4AllEmbeddings(model_file="/Users/mac/Downloads/all-MiniLM-L6-v2-f16.gguf")
        db = FAISS.from_documents(chunks, embedding_model)
        db.save_local(f"{self.vector_db_path}/{random_number}")
        return f"{self.vector_db_path}/5"
    def handle_file_pdf():
        return None


