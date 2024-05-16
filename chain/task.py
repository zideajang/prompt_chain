from abc import ABC
from typing import List,Callable

from agent import Agent
from 

class Task(ABC):
    def __init__(self,
                 name:str,
                 description:str,
                 agents:List[Agent],
                 target_fn:Callable[[str],bool]
                 ) -> None:
        self.name = name
        self.description = description
        self.agents = agents
        self.target_fn = target_fn

    async def invoke(self,input:Messages)
class PlanTask(Task):


    def plan(self):
        pass



if __name__ == "__main__":
    pass

