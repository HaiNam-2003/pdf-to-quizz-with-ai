from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers.regex import RegexParser

class ModelService():
    def __init__(self) -> None:
        self.llm_file =  "E:/python/pdf-to-quizz/model_data/all-MiniLM-L6-v2-f16.gguf"
        self.embedding_model_file = "E:/python/pdf-to-quizz/model_data/all-MiniLM-L6-v2-f16.gguf"
        self.template = """<|im_start|>system\n\n
        {context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant"""
        self.output_parser = RegexParser(
    regex=r"Question\s?\d?:\s+\n?(.*?)\nCHOICE_A(.*?)\nCHOICE_B(.*?)\nCHOICE_C(.*?)\nCHOICE_D(.*?)(?:\n)+Answer:\s?(.*)\n?\n?Question\s?\d?:\s+\n?(.*?)\nCHOICE_A(.*?)\nCHOICE_B(.*?)\nCHOICE_C(.*?)\nCHOICE_D(.*?)(?:\n)+Answer:\s?(.*)", 
    output_keys=["question1", "A_1", "B_1", "C_1", "D_1", "reponse1","question2", "A_2", "B_2", "C_2", "D_2", "reponse2"]
)
    def loadLLM(self):
        GOOGLE_API_KEY = "AIzaSyBKiReCTYg1L_EX7SypuRbclomM0lrSSL4"
        llm = ChatGoogleGenerativeAI(model="gemini-pro",
                 temperature=0.1, top_p=0.85, google_api_key=GOOGLE_API_KEY)
        return llm
    def create_prompt(self):
        prompt = PromptTemplate(template = self.template,input_variables=["context", "question"])
        return prompt
    def create_qa_chain(self,db):
        llm_chain = RetrievalQA.from_chain_type(
            llm=self.loadLLM(),
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k":3}, max_tokens_limit=1024),
            return_source_documents=True,
            chain_type_kwargs={
                'prompt': self.create_prompt()
                } )
        return llm_chain
    def read_vectors_db(self,vector_db_path):
        embedding_model = GPT4AllEmbeddings(model_file=self.embedding_model_file)
        db = FAISS.load_local(vector_db_path, embedding_model, allow_dangerous_deserialization=True)
        return db
    def respone(self,file_data_path):
        db = self.read_vectors_db(vector_db_path=file_data_path)
        llm_chain = self.create_qa_chain(db=db)
        query = """You are a teacher preparing questions for a quiz. Given the following document, please generate 10 multiple-choice questions (MCQs) with 4 options and a corresponding answer letter based on the document.The response only bellow example. The response is translate to VietNamese
            Example question:
            
            <start question>
            Question here
            A: choice here
            B: choice here
            C: choice here
            D: choice here
            Answer: A or B or C or D
            <end question>
            
            These questions should be detailed and solely based on the information provided in the document.
        """
        response = llm_chain.invoke({"query": query})
        return response
    