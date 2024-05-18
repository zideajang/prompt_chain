import os
import json

from abc import ABC,abstractmethod

from typing import Optional,Dict

from promptchain.config import PromptChainConfig

config = PromptChainConfig()


class StorageConnector(ABC):
    
    def __init__(self,user_id,agent_id=None) -> None:
        self.user_id = user_id
        self.agent_id = agent_id
        self.storage = {}
    
    @staticmethod
    def get_storage_connector(storage_type,config,user_id, agent_id):
        return SimpleJSONStorageConnector(config,user_id,agent_id)

    @staticmethod
    def get_recall_storage_connector(user_id, agent_id):

        return StorageConnector.get_storage_connector("json", config, user_id, agent_id)
    
    @abstractmethod
    def get_all(self, filters: Optional[Dict] = {}, limit=10):
        pass


class SimpleJSONStorageConnector(StorageConnector):

    def __init__(self,config,user_id,agent_id=None) -> None:
        json_path =  f"{config.archival_storage_path}/{user_id}.json"
        if os.path.exists(json_path):
            with open(json_path,"r") as f:
                self.json_data = json.load(f) 
        
    def get_all(self, filters: Optional[Dict] = {}, limit=10):
        pass
