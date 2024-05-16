from pydantic import BaseModel
from message import Message,AIMessage,HumanMessage,SystemMessage,Messages

class MessagePromptTemplate(BaseModel):
    template:str
    @classmethod
    def from_template(cls,template:str):
        return cls(template=template)
    

class AIMessagePromptTemplate(MessagePromptTemplate):

    async def invoke(self,messages:Messages)->Message:
        return AIMessage(content=self.template)
    
class HumanMessagePromptTemplate(MessagePromptTemplate):

    async def invoke(self,messages:Messages)->Message:
        return HumanMessage(content=self.template)

