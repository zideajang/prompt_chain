from abc import ABC



"""
计算生成 token 
多轮对话 token 不断增加，token 达到 LLM 上限，发生 system warm 信号
抽取信息,压缩信息，LLM 调用方法保存本地，保存过程，会议有一个更新
"""
class BaseMemory(ABC):
    def __init__(self,name) -> None:
        self.name = name

    
    def save(self,Messages):
        pass

# long term memory
class PersistentMemory(BaseMemory):


    
    
    def read_file(self,name):
        pass

    def write_file(self,content):
        pass
    
    def update(self):
        pass
# short term memory
class CacheMemory:

    def load(self,content):
        pass

    def update(self):
        pass




