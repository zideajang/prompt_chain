
import inspect
import asyncio
import ollama
from ollama import AsyncClient
from rich.console import Console


from promptchain.message import Message,Messages,AIMessage

from promptchain.constants import INITIAL_BOOT_MESSAGE

console = Console()
from rich.markdown import Markdown

def build_model(model):
    def invoke(prompt):
        response = ollama.chat(
            model=model,
            messages=[{
                "role":"user",
                "content":prompt
            }]
        )
        return response['message']['content']
    return invoke


def build_embedding_model(model_name:str):
    def invoke(prompt_str:str):
        response = ollama.embeddings(model=model_name, prompt=prompt_str)
        return response["embedding"]
    
    return invoke

def build_chat_message_model(model_name:str):
    def intial_system(system_content:str):
        def intial_assistent(asistent_content:str):
            def invoke(prompt_str:str):
                response =  ollama.chat(
                    model=model_name,
                    messages=[
                        {
                            "role":"system",
                            "content":system_content
                        },
                         {
                            "role":"assistant",
                            "content":asistent_content
                        },
                        {
                            "role":"user",
                            "content":prompt_str
                        }]
                )
                return response['message']['content']
            
            return invoke
        return intial_assistent
    return intial_system


def build_chat_model(model_name:str):
    def intial_system(system_content:str):
        async def invoke(prompt_str:str):
            response =  ollama.chat(
                model=model_name,
                messages=[
                    {
                        "role":"system",
                        "content":system_content
                    },
                    {
                        "role":"user",
                        "content":prompt_str
                    }]
            )
            return response['message']['content']
        return invoke
    return intial_system




class ChatMessageModel:

    def __init__(self,model_name) -> None:
        self.model_name = model_name

    def ask(self,messages:Messages):
        pass

    async def invoke(self,messages:Messages):
        console.print(messages.model_dump()['messages'])
        response = ollama.chat(
            model=self.model_name,
            messages=messages.model_dump()['messages']
        )

        return  AIMessage(content=response['message']['content']) 



if __name__ == "__main__":
    
    response = build_chat_message_model("llama3")(INITIAL_BOOT_MESSAGE)("You are a helpful AI assistant.Solve tasks using your coding and language skills.")("write hello world in java")
    
    console.print(response)

    # response = build_model("llama3")("write read csv file in python")
    # console.print(Markdown(response))

    # response = build_chat_model("llama3")("you are linux operating system")("ls command")
    # console.print(Markdown(response))


