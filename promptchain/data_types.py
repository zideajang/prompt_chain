import uuid

class AgentState:

    def __init__(self,
            name,
            persona,
            human,
            user_id: uuid.UUID,
            agent_id:uuid.UUID
                 ) -> None:
        self.name = name
        self.persona = persona
        self.human = human
        self.user_id = user_id
        self.agent_id = agent_id