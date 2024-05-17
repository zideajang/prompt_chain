import asyncio

from abc import ABC
from typing import Optional,Callable,Any

from rich.console import Console
from rich.prompt import Prompt

from promptchain.llm import ChatMessageModel,build_chat_model
from promptchain.message import SystemMessage,Message,AIMessage
from promptchain.chain_processor import ChainProcessor
from promptchain.memory.memory import BaseMemory

console = Console()

default_system_message = SystemMessage

DEFAULT_SYSTEM_MESSAGE = """You are a helpful AI assistant.
Solve tasks using your coding and language skills.
In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.
    1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.
    2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.
Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.
When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.
If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.
If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.
Reply "TERMINATE" in the end when everything is done.
"""

DEFAULT_DESCRIPTION = "A helpful and general-purpose AI assistant that has strong language skills, Python skills, and Linux command line skills."

class Agent(ABC):

    def __init__(self,
            name:str,
            llm, 
            is_termination_ms,
            memory:BaseMemory,#应该是一个接口，memoryclient
            system_message:SystemMessage) -> None:
        pass


class ConversationAgent(Agent):
    pass

class AgentState:
    pass

class UserProxyAgent(Agent):
    def __init__(self, 
                    name: str, 
                    llm, 
                    is_termination_msg, 
                    memory: BaseMemory, 
                    system_message: SystemMessage) -> None:
        super().__init__(name, llm, is_termination_msg, memory, system_message)
        self.llm = build_chat_model("llama3")(system_message.content)
        self.is_termination_msg = is_termination_msg

    async def query(self,message:Message):
        rsp = await self.llm(message.content)
        console.print(":robot:")
        console.print(rsp)
        console.print("-"*50)
        human_input = Prompt.ask("Enter your suggest if input exit and quit()")
        
        if self.is_termination_msg(human_input):
            return (rsp,True)

        return (f"{{'previous prompt':'{rsp}','suggest':'{human_input}' }}, respone format in JSON",False)

    async def a_query(self,message:Message):
        pass



if __name__ == "__main__":
    system_message = SystemMessage(content="you are very help assistant")
    ai_message = AIMessage(content="help write hello world in python")
    def termination_msg(message:str):
        return True
    user_proxy_agent = UserProxyAgent(name="test_agent 🚀",
                                      llm=build_chat_model,
                                      is_termination_msg=termination_msg,
                                      memory=BaseMemory("test_agent_memory"),
                                      system_message=system_message)

    asyncio.run(user_proxy_agent.query(ai_message))
    console.print("start conversation...")
