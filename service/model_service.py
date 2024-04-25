from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

class ModelService():
    def __init__(self) -> None:
        self.llm_file =  "/Users/mac/Downloads/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf"
        self.embedding_model_file = "/Users/mac/Downloads/all-MiniLM-L6-v2-f16.gguf"
        self.template = """<|im_start|>system\n\n
        {context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant"""
    def loadLLM(self):
        GOOGLE_API_KEY = "AIzaSyBKiReCTYg1L_EX7SypuRbclomM0lrSSL4"
        llm = ChatGoogleGenerativeAI(model="gemini-pro",
                 temperature=0.7, top_p=0.85, google_api_key=GOOGLE_API_KEY)
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
                'prompt': self.create_prompt()}
        )
        return llm_chain
    def read_vectors_db(self,vector_db_path):
        embedding_model = GPT4AllEmbeddings(model_file=self.embedding_model_file)
        db = FAISS.load_local(vector_db_path, embedding_model, allow_dangerous_deserialization=True)
        return db
    def respone(self,file_data_path):
        db = self.read_vectors_db(vector_db_path=file_data_path)
        llm_chain = self.create_qa_chain(db=db)
        query = """You are a teacher preparing questions for a quiz. Given the following document, please generate 20 multiple-choice questions (MCQs) with 4 options and a corresponding answer letter based on the document.The response only bellow example. The response is translate to VietNamese
        ''Example:
        Question1: What is the individual's name who stated they want to be a DevOps Engine er?
        CHOICE_A: Huynh Ngoc Huy
        CHOICE_B: VietHan Korea
        CHOICE_C: DevOps Engineer
        CHOICE_D: Feature
        Answer: A''
        """
        response = llm_chain.invoke({"query": query})
        return response