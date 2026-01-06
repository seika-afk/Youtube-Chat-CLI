from document_ingestion import execute
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split(uri):
    transcript=execute(uri)
    
    docs=[Document(
            page_content=snippet.text,
            metadata={
                "start":snippet.start,
                "duration":snippet.duration

                }
            )
          for snippet in  transcript
          ]
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunks_=splitter.split_documents(docs)
    return chunks_



