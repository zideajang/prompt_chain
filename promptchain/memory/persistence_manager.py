from abc import ABC,abstractmethod
from promptchain.utils import get_local_time,printd


class PersistenceManager(ABC):
    @abstractmethod
    def trim_messages(self, num):
        pass

    @abstractmethod
    def prepend_to_messages(self,added_messages):
        pass
    @abstractmethod
    def append_to_messages(self,added_messages):
        pass


class LocalStateManager(PersistenceManager):

    def __init__(self,agent_state) -> None:
        self.memory = None
        self.archival_memory = []
        self.recall_memory = []