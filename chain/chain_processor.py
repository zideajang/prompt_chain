from abc import ABC,abstractmethod

from typing import Any,Protocol

import asyncio

from pydantic import BaseModel,Field
from dataclasses import dataclass

from llm import ChatMessageModel
from message import Message,SystemMessage,HumanMessage,AIMessage,Messages
from prompt import AIMessagePromptTemplate,HumanMessagePromptTemplate

class Runnable(Protocol):
    async def invoke(self,messages:Messages)->Message:
        ...
    

@dataclass
class ChainProcessor:
    chain_list:list[Runnable] 
    messages:Message

    def __init__(self,messages:Message):
        self.chain_list = []
        self.messages = messages

    def __or__(self, runnable: Runnable):
        self.chain_list.append(runnable)
        return self

    async def invoke(self):
        for runnable in self.chain_list:
            rsp = await runnable.invoke(self.messages)
            self.messages.add_message(rsp)

async def main():
    system_message = SystemMessage(content="you are linux system")
    
    assistant_message = AIMessagePromptTemplate.from_template("you are very help assistant")
    humam_message = HumanMessagePromptTemplate.from_template("ls")

    model = ChatMessageModel("llama3")
    
    chain = ChainProcessor(Messages(messages=[system_message]))
    
    chain | assistant_message | humam_message | model
    await chain.invoke()
    print(chain.messages)

if __name__ == "__main__":
    asyncio.run(main())