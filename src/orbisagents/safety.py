"""Agent safety gates independent of model providers."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AgentAction:
    agent: str
    action: str
    requires_approval: bool = False

def requires_human_approval(action: AgentAction) -> bool:
    return action.requires_approval or action.action.lower() in {"publish", "delete", "transfer"}