# # from callback import MyCallbackHandler
# from langchain.callbacks.base import BaseCallbackManager
# from langchain_community.llms import CTransformers
# from llm_chain import QCMGenerateChain


# class QaLlm():

#     def __init__(self) -> None:
#         self.llm = CTransformers(
#         model="/Users/mac/Downloads/vinallama-7b-chat_q5_0.gguf",
#         max_new_tokens=1024,
#         temperature=0.1
#     )
#     def get_llm(self):
#         return self.llm
# qa_llm = QaLlm()
# qa_chain = QCMGenerateChain.from_llm(qa_llm.get_llm())
# print(qa_chain.invoke({"doc":"My name is Huy"}))
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
from service.test.llm_chain import QCMGenerateChain
from langchain.output_parsers.regex import RegexParser

# Cau hinh
model_file = "/Users/mac/Downloads/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf"
vector_db_path = "vectorstores/db_faiss"

# Load LLM
def load_llm(model_file):
    llm = CTransformers(
        model=model_file,
        model_type="llama",
        max_new_tokens=1024,
        temperature=0.01
    )
    return llm

# Tao prompt template
def creat_prompt():
    template = """You are a teacher preparing questions for a quiz. Given the following document, please generate 2 multiple-choice questions (MCQs) with 4 options and a corresponding answer letter based on the document.The response only bellow example 
        ''Example:
        Question1: What is the individual's name who stated they want to be a DevOps Engineer?
        CHOICE_A: Huynh Ngoc Huy
        CHOICE_B: VietHan Korea
        CHOICE_C: DevOps Engineer
        CHOICE_D: Feature
        Answer: A''
        <Begin Document>
        {doc}
        <End Document>"""
    output_parser = RegexParser(
            regex=r"Question\s?\d+:\s+(.*?)\nCHOICE_A: (.*?)\nCHOICE_B: (.*?)\nCHOICE_C: (.*?)\nCHOICE_D: (.*?)(?:\n)+Answer:\s?(.*)\n\nQuestion\s?\d+:\s+(.*?)\nCHOICE_A: (.*?)\nCHOICE_B: (.*?)\nCHOICE_C: (.*?)\nCHOICE_D: (.*?)(?:\n)+Answer:\s?(.*)",
            output_keys=["Question1", "A_1", "B_1", "C_1", "D_1", "reponse1", "question2", "A_2", "B_2", "C_2", "D_2", "reponse2"]
        )

    PROMPT = PromptTemplate(
            input_variables=["doc"],template=template
        )
    return PROMPT
# Tao simple chain
# def create_qa_chain(llm):
#     llm_chain = QCMGenerateChain.from_llm(
#         llm = llm
#     )
#     return llm_chain
def create_qa_chain(prompt, llm, db):
    llm_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 3}, max_tokens_limit=1024),
        return_source_documents=False,
        chain_type_kwargs={'prompt': prompt, 'document_variable_name': 'doc'}
    )
    return llm_chain

def result() -> str:
    print("hello")
    llm = load_llm(model_file)
    embedding_model = GPT4AllEmbeddings(model_file="/Users/mac/Downloads/all-MiniLM-L6-v2-f16.gguf")
    db = FAISS.load_local(vector_db_path, embedding_model, allow_dangerous_deserialization=True)
    prompt = creat_prompt()

    llm_chain  =create_qa_chain(prompt=prompt,llm=llm,db=db)

    # Chay cai chain
    question = "Create multi choose"
    # question = "what your name?"
    response = llm_chain.invoke({"query": question})
    print(f"huy {response}")
    return "hello"

# print(result())