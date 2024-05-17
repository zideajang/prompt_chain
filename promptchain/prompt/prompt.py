from typing import Dict,Optional,List

from pydantic import BaseModel

from promptchain.message import Message,AIMessage,HumanMessage,SystemMessage,Messages

class MessagePromptTemplate(BaseModel):
    template:str

    @classmethod
    def from_template(cls,template:str):
        return cls(template=template)
    
    def format(self,**kwargs):
        print(kwargs)
        return self.template.format(**kwargs)

class SystemMessagePromptTemplate(MessagePromptTemplate):
 
    async def invoke(self,messages:Messages)->Message:
        return SystemMessage(content=self.template)

class AIMessagePromptTemplate(MessagePromptTemplate):

    async def invoke(self,messages:Messages)->Message:
        return AIMessage(content=self.template)
    
class HumanMessagePromptTemplate(MessagePromptTemplate):

    async def invoke(self,messages:Messages)->Message:
        return HumanMessage(content=self.template)


if __name__ == "__main__":
    prompt_template = AIMessagePromptTemplate.from_template("Generate a clickworthy title about this topic:'{base_info}'Respond in JSON format {{title: 'title', topic: '{base_info}'}}")
    res = prompt_template.format(base_info="function programming")
    print(res)
    