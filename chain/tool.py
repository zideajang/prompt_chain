from typing import Protocol,List
from abc import ABC
from message import Messages,Message

from rich.console import Console
from rich.markdown import Markdown
from tiktoken._educational import *
console = Console()

class Tool(ABC):
    def __init__(self,name,description) -> None:
        self.name = name
        self.description = description
    async def invoke(self,messages:Messages)->Message:
        ...

class CalcTokenTool(Tool):

    def __init__(self, name, description) -> None:
        super().__init__(name, description)
        self.enc = SimpleBytePairEncoding.from_tiktoken("cl100k_base")

    async def invoke(self,messages:Messages)->Message:
        total_content = ""
        for message in messages:
            total_content += message.content

        print(self.enc.encode(total_content))

class PrintMarkdownTool(Tool):

    async def invoke(self,messages:Messages)->Message:
        message = messages.messages[-1]
        if isinstance(message,Message):
            console.print(Markdown(message.content))
        else:
            console.print(message.content)
        return None

class PrintJsonTool(Tool):
    
    async def invoke(self,messages:Messages)->Message:
        message = messages.messages[-1]
        if isinstance(message,Message):
            console.print_json(message.json())
        else:
            console.print(message.content)
        return None