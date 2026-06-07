class AgentChat:
    """
    This is supposed to represent a chat app where the agents can converse with one another. For ease of implementation's sake, for right now, the chat is gonna assume a synchronous messaging system. It also keeps track of the unseen messages for each agent.
    """
    def __init__(self, manager) -> None:
        self.messages = []
        self.members = []
        self.unseen_count = {}
        self.total_msgs = 0
        self.manager = manager

    def add_member(member: str) -> None:
        self.members.append(member)
        self.unseen_count[member] = self.total_messages

    def read_unseen(member: str) -> list[dict[str, str]]:
        msg_count = self.unseen_count[member] 
        return messages[-msg_count]

    def read_seen(prev_count: int = None) list[dict[str, str]]:
        if prev_count is not None:
            return self.messages[-prev_count]
        
        return self.messages

    def send_message(member: str, content: str) -> None:
        self.messages.append({member: content})
        self.total_messages += 1
        for count in self.unseen_count.values():
            count += 1



