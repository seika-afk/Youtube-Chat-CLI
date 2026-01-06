from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_community.vectorstores.faiss import FAISS
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def retriever(text):
    vector_store=FAISS.load_local(
            "faiss_index",
            embedding,
            allow_dangerous_deserialization=True
            )
    retriever=vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={"k": 6, "lambda_mult": 0.5}


            )
    result=retriever.invoke(text)
    return result
