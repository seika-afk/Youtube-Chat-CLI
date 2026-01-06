from langchain_community.embeddings import HuggingFaceEmbeddings 
from text_splitting import split
from langchain_community.vectorstores.faiss import FAISS
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")




def store_vec(uri):
    doc=split(uri)
    if  doc :
    
        vector_store=FAISS.from_documents(split(uri),embedding=embedding)
        vector_store.save_local("faiss_index")
