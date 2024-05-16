from typing import Union,List
import asyncio
from rich.console import Console
from rich.markdown import Markdown
from message import Message,Messages,AIMessage
from prompt import AIMessagePromptTemplate,SystemMessage,SystemMessagePromptTemplate,MessagePromptTemplate
from llm import ChatMessageModel

console = Console()

class SnowballChain:
    def __init__(self,templates:List[Union[str,MessagePromptTemplate]]) -> None:
        
        self.messages:Messages = Messages(messages=[])
        self.templates:List[Union[str,MessagePromptTemplate]] = templates

        self.llm = ChatMessageModel("llama3")
        

    async def invoke(self,**kwargs):

        # intial start 
        ai_message = AIMessage(content=self.templates[0].format(**kwargs))
        self.messages.messages.append(ai_message)

        rsp = await self.llm.invoke(messages=self.messages)
        console.print(Markdown(rsp.content))
        self.messages.messages.append(rsp)

        for prompt_template in self.templates[1:]:

            assistent_template = prompt_template.format(response=self.messages.messages[-1].content)
            request_messages = Messages(messages=[AIMessage(content=assistent_template)])
            
            rsp = await self.llm.invoke(request_messages)
            console.print(Markdown(rsp.content))

            self.messages.messages.append(rsp)


async def main():

    prompt_tempalte_list = [
        AIMessagePromptTemplate.from_template(template="Generate a clickworthy title about this topic:'{base_info}'Respond in JSON format {{title: 'title', topic: '{base_info}'}}"),
        AIMessagePromptTemplate.from_template("Generate a compelling 3 section outline given this information: '{response}'. Respond in JSON format {{title: '<title>', topic: '<topic>', sections: ['<section1>', '<section2>', '<section3>']}}"),
        AIMessagePromptTemplate.from_template("Generate 1 paragraph of content for each section outline given this information: '{response}'. Respond in JSON format {{title: '<title>', topic: '<topic>', sections: ['<section1>', '<section2>', '<section3>'], content: ['<content1>', '<content2>', '<content3>']}}"),
        AIMessagePromptTemplate.from_template("Generate a markdown formatted blog post given this information: '{response}'. Respond in JSON format {{markdown_blog: '<entire markdown blog post>'}}")
    ]

    snowball_chain = SnowballChain(templates=prompt_tempalte_list)
    await snowball_chain.invoke(base_info="function programming")

if __name__ == "__main__":
    asyncio.run(main())