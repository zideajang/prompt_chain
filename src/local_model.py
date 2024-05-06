# import ollama
from typing import Protocol,List
import functools


class BaseMessags:
    pass

class LLMResponse:
    pass

class LLMFunction:
    pass

class BaseLLM(Protocol):
    def invoke(self,prompt:str)->LLMResponse:
        pass

    def ainvoke(self,prompt:str)->LLMResponse:
        pass

    def stream(self,prompt:str)->LLMResponse:
        pass

    def bind_functions(self,functions:List[LLMFunction]):
        pass


class LLM:

    @property
    def _llm_type(self) -> str:
        return "llama"
    


def build_model(model):
    return functools.partial(func) 


# def build_ollama_model(model,prompt):
#     response = ollama.chat(
#         model=model,
#         messages=[{
#             "role":"user",
#             "content":prompt
#         }]
#     )

#     return response['message']['content']

if __name__ == "__main__":
    llm = LLM()