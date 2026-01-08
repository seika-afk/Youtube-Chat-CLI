
import  pyfiglet
from main import call as call_
from main import add_faiss_index
from InquirerPy import inquirer
from rich import print
from rich.panel import Panel
from subprocess import call
import time
import sys
def intro():
    pyfiglet.Figlet("big")
    f=pyfiglet.figlet_format("yat",font="starwars")
    print(f)


def decision():
    query=inquirer.select(
            message="Choose : ",
            choices=["> Previous Video","> New Video"]

            ).execute()

    return query

def chat_loop():
    while True:
        q= input("> ")
        if q=="q":
            sys.exit()
        print("Waiting...")
        call_(q)
    time.sleep(0.2)
    print("exiting...")
    time.sleep(0.2)
    sys.exit()

def qoc():
    query=inquirer.select(
            message="Choose : ",
            choices=["> Exit","> Chat"]

            ).execute()

    return query


def start_chat():
    print("> Entering Chat Mode in ...")
    time.sleep(0.3)
    print("3",end=" ")
    time.sleep(0.2)
    print(".",end="")
    time.sleep(0.1)
    print("2",end=" ")
    time.sleep(0.2)
    print(".",end="")
    time.sleep(0.1)
    print("1",end="")
    call("clear")


def main_loop():
    intro()
    query=decision()
    if query == "> Previous Video":
        start_chat()
        chat_loop()
    else:
        print("> Enter Youtube Link : ")
        link=input(">> ")
        print(Panel("Wait while we are creating Vector Store for fast retrieval [3-5m]"))
        print("> Waiting...")
        add_faiss_index(link)
        print("> Added Faiss Index")

        qoc_=qoc()
        if qoc_== "> Exit":
            sys.exit()
        start_chat()
        chat_loop()



main_loop()


#uri="https://www.youtube.com/watch?v=0cZxl7RLFhs"
#print("adding faiss vecs")
#add_faiss_index(uri)
#print("added faiss")
#call("what is this video about?")
