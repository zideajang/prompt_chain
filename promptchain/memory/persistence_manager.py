from abc import ABC,abstractmethod
from promptchain.utils import get_local_time,printd


class PersistenceManager(ABC):
    @abstractmethod
    def trim_messages(self, num):
        pass


class InMemoryStateManager(PersistenceManager):

    def __init__(self) -> None:
        self.memory = None
        self.messages = []
        self.all_messages = []