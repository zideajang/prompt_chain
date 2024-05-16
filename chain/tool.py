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
