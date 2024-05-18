import uuid

from datetime import datetime
from typing import Optional,Dict
from config import LLMConfig,EmbeddingConfig

class AgentState:
    def __init__(self,
            id:uuid.UUID,
            name:str,
            llm_config:LLMConfig,
            embedding_config:EmbeddingConfig,
            persona:str, #then filename where save agent profile and detail
            human:str, #the filename where save user detail
            state:Optional[dict] = None,
            created_at:Optional[datetime] = None) -> None:
        
        
        if id is None:
            self.id = uuid.uuid4()
        else:
            self.id = id

        self.name = name

        self.persona = persona
        self.huamn = human

        self.llm_config = llm_config
        self.embedding_config = embedding_config


        self.created_at = created_at if created_at is not None else datetime.now()
        self.state = {} if not state else state


