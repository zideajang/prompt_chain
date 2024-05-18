from abc import ABC,abstractmethod
from typing import List,Callable,Union
import asyncio

from rich.console import Console
from promptchain.agent.agent import Agent,UserProxyAgent
from promptchain.chain_processor import ChainProcessor
from promptchain.llm import ChatMessageModel,build_chat_model
from promptchain.message import SystemMessage,Message,AIMessage
from promptchain.memory.memory import BaseMemory


"""
TODO
- 在 task 中 agent 的工作协调应该如何解决
- task , langgraph
- 在 task 中，首先设定有一个目标(description)
"""

console = Console()

class Task(ABC):
    def __init__(self,
                 name:str,
                 description:str,
                 agent:Union[Agent,List[Agent]],
                 target_fn
                 ) -> None:
        self.name = name
        self.description = description
        self.agent = agent
        self.target_fn = target_fn

    @abstractmethod
    def run(self):
        pass
        


    @abstractmethod
    async def a_run(self):
        pass

class ChatTask(Task):
    def __init__(self, 
                 name: str, 
                 description: str, 
                 agent: Union[Agent,List[Agent]], 
                 target_fn) -> None:
        super().__init__(name, description, agent, target_fn)

    async def start(self):
        ai_message = AIMessage(content="write hello world promgram in java")

        
        console.print(f":boy:\t [blue]{ai_message.content}[/]")
        while(True):
            rsp,res = await self.agent.query(ai_message)
            
            console.print(f"{res=}")
            console.print(":robot:")
            console.print(rsp)

            if(res):
                console.print(":robot: \t [bold blue]quit[/]")
                break
            else:
                ai_message = AIMessage(content=rsp)

    def run(self):
        pass

    async def a_run(self):
        while(True):
            rsp,res = self.agents[0].query()
           

class PlanAndExcuteTask(Task):
    def plan(self):
        pass



if __name__ == "__main__":
    system_message = SystemMessage(content="you are very help assistant")
    ai_message = AIMessage(content="help write hello world in python")

    def termination_msg(message:str):
        if message == "exit" or message == "quit":
            return True
        return False

    user_proxy_agent = UserProxyAgent(name="test_agent 🚀",
                                      llm=build_chat_model,
                                      model_name="llama3",
                                      is_termination_fn=termination_msg,
                                      memory=BaseMemory("test_agent_memory"),
                                      system_message=system_message)

    chat_task = ChatTask(name="chatbot",
                         description="help write hello world in python",
                         agent=user_proxy_agent,
                         target_fn=None)

    asyncio.run(chat_task.start())

