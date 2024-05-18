from abc import ABC,abstractmethod
from promptchain.message import Message
from promptchain.storage import StorageConnector
from promptchain.llm import build_chat_model

"""
TODO
在 chatTask 将记忆引入
计算生成 token 
多轮对话 token 不断增加，token 达到 LLM 上限，发生 system warm 信号
抽取信息,压缩信息，LLM 调用方法保存本地，保存过程，会议有一个更新

BaseMemory 会有记忆功能
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

class RecallMemory(ABC):
    @abstractmethod
    def text_search(self,query_str,count=None,start=None):
        ...

    @abstractmethod
    def date_search(self, start_date, end_date, count=None, start=None):
        """Search messages between start_date and end_date in recall memory"""

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def insert(self, message: Message):
        """Insert message into recall memory"""

class BaseRecallMemory(RecallMemory):
    
    def __init__(self,agent_state) -> None:
        self.agent_state = agent_state
        self.storage = StorageConnector.get_recall_storage_connector(
            user_id=agent_state.user_id, 
            agent_id=agent_state.id)
        
        # self.embed_model = 

