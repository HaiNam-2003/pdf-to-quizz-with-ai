from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import GPT4AllEmbeddings

def read_data_from_faiss(faiss_file_path):
    # Load the FAISS vector store with dangerous deserialization enabled
    faiss_db = FAISS.load_local(faiss_file_path,GPT4AllEmbeddings(), allow_dangerous_deserialization=True)

    # Get the number of vectors in the FAISS database
    num_documents = len(faiss_db.index_to_docstore_id)

    return num_documents

# Example usage
faiss_file_path = "/Users/mac/Documents/Final Project/app/data/vectorstore/5"
num_vectors = read_data_from_faiss(faiss_file_path)
print("Number of vectors in FAISS:", num_vectors)
