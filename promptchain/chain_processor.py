from abc import ABC,abstractmethod

from typing import Any,Protocol,List

import asyncio

from pydantic import BaseModel,Field
from dataclasses import dataclass

from promptchain.llm import ChatMessageModel
from promptchain.message import Message,SystemMessage,HumanMessage,AIMessage,Messages
from promptchain.prompt.prompt import AIMessagePromptTemplate,HumanMessagePromptTemplate
from promptchain.tool import PrintJsonTool,PrintMarkdownTool,ExtractCodeTool

class Runnable(Protocol):
    async def invoke(self,messages:Messages)->Message:
        ...
    

@dataclass
class ChainProcessor:
    chain_list:List[Runnable] 
    is_sequence:bool
    messages:Message

    def __init__(self,messages:Message):
        self.chain_list = []
        self.is_sequence = False
        self.messages = messages

    def __or__(self, runnable: Runnable):
        self.chain_list.append(runnable)
        return self

    async def invoke(self):
        for runnable in self.chain_list:
            if(self.is_sequence):
                messages = self.messages[-1]
            else:
                messages = self.messages
            rsp = await runnable.invoke(messages)
            if rsp is not None:
                self.messages.add_message(rsp)

async def simple_chain_example():
    system_message = SystemMessage(content="you are linux system")
    
    assistant_message = AIMessagePromptTemplate.from_template("you are very help assistant")
    humam_message = HumanMessagePromptTemplate.from_template("ls")

    model = ChatMessageModel("llama3")
    
    chain = ChainProcessor(Messages(messages=[system_message]))

    print_markdown_tool = PrintMarkdownTool(name="print markdown",description="print markdown")
    
    # task [task agent[prompt | model | response] | agent[prompt | model | respone] outputcheck(target fn)-> task
    chain | assistant_message | humam_message | model | print_markdown_tool
    await chain.invoke()
    print(chain.messages)

async def simple_code_example():
    system_message = SystemMessage(content="you are python expert")

    assistant_message = AIMessagePromptTemplate.from_template("you are very help assistant")
    humam_message = HumanMessagePromptTemplate.from_template("write read file programming in python")

    model = ChatMessageModel("llama3")
    
    chain = ChainProcessor(Messages(messages=[system_message]))

    print_markdown_tool = PrintMarkdownTool(name="print markdown",description="print markdown")
    extract_code_tool = ExtractCodeTool(name="extract code",description="extract code from response")

    # task [task agent[prompt | model | response] | agent[prompt | model | respone] outputcheck(target fn)-> task
    chain | assistant_message | humam_message | model | print_markdown_tool| extract_code_tool
    await chain.invoke()
    print(chain.messages)

if __name__ == "__main__":
    asyncio.run(simple_code_example())