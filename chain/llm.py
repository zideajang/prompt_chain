
import inspect

import ollama

from rich.console import Console
from message import Message,Messages,AIMessage
console = Console()

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
        def invoke(prompt_str:str):
            response = ollama.chat(
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

    async def invoke(self,messages:Messages):
        response = ollama.chat(
            model=self.model_name,
            messages=messages.model_dump()['messages']
        )
        return  AIMessage(content=response['message']['content']) 



if __name__ == "__main__":
    response = build_model("llama3")("write read csv file in python")
    print(response)

    response = build_chat_model("llama3")("you are linux operating system")("ls command")
    console.print(response)