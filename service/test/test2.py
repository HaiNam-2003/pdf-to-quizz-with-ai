from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Cau hinh
model_file =  "/Users/mac/Downloads/Hermes-2-Pro-Mistral-7B.Q5_K_M.gguf"
vector_db_path = "/Users/mac/Documents/Final Project/app/service/test/vectorstores/db_faiss"

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
def creat_prompt(template):
    prompt = PromptTemplate(template = template, input_variables=["context", "question"])
    return prompt


# Tao simple chain
def create_qa_chain(prompt, llm, db):
    llm_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k":3}, max_tokens_limit=1024),
        return_source_documents=True,
        chain_type_kwargs={
            'prompt': prompt
            }
    )
    return llm_chain


# Read tu VectorDB
def read_vectors_db():
    # Embeding
    embedding_model = GPT4AllEmbeddings(model_file="/Users/mac/Downloads/all-MiniLM-L6-v2-f16.gguf")
    db = FAISS.load_local(vector_db_path, embedding_model, allow_dangerous_deserialization=True)
    return db


def test():
# Bat dau thu nghiem
    db = read_vectors_db()
    llm = load_llm(model_file)

    #Tao Prompt
    template = """<|im_start|>system\n\n
        {context}<|im_end|>\n<|im_start|>user\n{question}<|im_end|>\n<|im_start|>assistant"""
    prompt = creat_prompt(template)

    llm_chain  =create_qa_chain(prompt, llm, db)

    # Chay cai chain
    query = """You are a teacher preparing questions for a quiz. Given the following document, please generate 2 multiple-choice questions (MCQs) with 4 options and a corresponding answer letter based on the document.The response only bellow example 
        ''Example:
        Question1: What is the individual's name who stated they want to be a DevOps Engineer?
        CHOICE_A: Huynh Ngoc Huy
        CHOICE_B: VietHan Korea
        CHOICE_C: DevOps Engineer
        CHOICE_D: Feature
        Answer: A''"""
    response = llm_chain.invoke({"query": query})
    return response