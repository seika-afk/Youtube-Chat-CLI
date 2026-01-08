#augmentation 
# template
# ask from qn
# give answer

import os
from dotenv import load_dotenv
from langchain_core._api.deprecation import LangChainDeprecationWarning
import warnings

warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)


load_dotenv()


def prepare_prompt(question):
    from retriever import retriever
    from langchain_core.prompts import PromptTemplate
    prompt = PromptTemplate(
        template="""
You are a precise and knowledgeable YouTube assistant.
You are given the context of a YouTube video (transcript, description, or captions).

Your task is to answer the question strictly based on the provided context.
- If the context is sufficient, give a direct, accurate, and factual answer.
- Keep answers concise but clear; include relevant details.
- Do NOT speculate or add information not present in the context.
- If the context is missing, unclear, or insufficient, reply exactly:
“I’m sorry, but I don’t have enough information to answer that.”
- Format your answer for terminal display; do not use Markdown.

Context:
{context}

Question:
{question}
"""
)    
    retrieved_docs = retriever(question)

    context_text = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    final_prompt = prompt.invoke(
        {
            "context": context_text,
            "question": question,
        }
    )

    return final_prompt



def add_faiss_index(uri):
    from vecStore import store_vec
    store_vec(uri)




def call(question):
    from huggingface_hub import InferenceClient
    from dotenv import load_dotenv
    client=InferenceClient(
            provider="novita",
            api_key=os.getenv("HF_TOKEN")
            )


    final_prompt=prepare_prompt(question)
    completion = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1",
        messages=[
            {
                "role": "user",
                "content": str(final_prompt)
            }
        ],
    )
    text=completion.choices[0].message.content

    if "</think>" in text:
        answer = text.split("</think>")[-1].strip()
        print(answer)
    else:
        print("No <think> block found.")






# to run
# first check if transcript exists or not
# first call add_faiss_index
# then call call() while giving question as param
def main():
    pass

if __name__ == "__main__":
    main()

