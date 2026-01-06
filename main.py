#augmentation 
# template
# ask from qn
# give answer

from vecStore import store_vec
from retriever import retriever
import os
from langchain_core.prompts import PromptTemplate

from huggingface_hub import InferenceClient
from dotenv import load_dotenv
load_dotenv()


print("starting..")
def prepare_prompt(question):
    prompt = PromptTemplate(
        template="""
You are a helpful and knowledgeable YouTube assistant.
You are given the context of a YouTube video (such as the transcript or description).

Based on this context, your job is to accurately answer questions related to the video.
If the context is clear and sufficient, provide a direct and informative answer.
If the context is missing or unclear, simply reply:
“I’m sorry, but I don’t have enough information to answer that.”
Try to answer in as few words as possible.But keep it detailed.
Be concise, factual, and avoid making assumptions beyond the provided context.




Context:
{context}

Question:
{question}
""",
        input_variables=["context", "question"],
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
    store_vec(uri)




def call(question):
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


uri="https://www.youtube.com/watch?v=0cZxl7RLFhs"
print("adding faiss vecs")
#add_faiss_index(uri)
print("added faiss")
call("what is this video about?")
