
import inspect
import asyncio
import ollama
from ollama import AsyncClient
from rich.console import Console


from promptchain.message import Message,Messages,AIMessage

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
    response = build_model("llama3")("write read csv file in python")
    console.print(Markdown(response))

    response = build_chat_model("llama3")("you are linux operating system")("ls command")
    console.print(Markdown(response))