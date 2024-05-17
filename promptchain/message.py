from typing import List
from pydantic  import BaseModel,Field
from rich.console import Console

console = Console()

class Message(BaseModel):
    role:str
    content:str

class AIMessage(Message):
    role:str = "assistant"
    content:str

class HumanMessage(Message):
    role:str = "user"
    content:str 

class SystemMessage(Message):
    role:str = "system"
    content:str 

class Messages(BaseModel):
    messages:List[Message]
    
    def add_message(self,message:Message):
        self.messages.append(message)
        
    def __add__(self,message:Message):
        self.messages.append(message)

if __name__ == "__main__":
    message = Message(role="user",content="write hello world in pythong")
    console.print(message.model_dump())
    console.print_json(message.json())

    ai_message = AIMessage(content="you are very help assistant")
    user_message = HumanMessage(content="write read csv file in python")
    
    console.print(ai_message.model_dump())

    messages = Messages(messages=[ai_message,user_message])
    console.print_json(messages.json())