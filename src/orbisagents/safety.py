"""Agent safety gates independent of model providers."""
from dataclasses import dataclass
SENSITIVE_ACTIONS = frozenset({"publish", "delete", "transfer"})
@dataclass(frozen=True)
class AgentAction:
    agent: str
    action: str
    requires_approval: bool = False
def requires_human_approval(action: AgentAction) -> bool:
    if not action.agent.strip() or not action.action.strip(): raise ValueError("agent and action are required")
    return action.requires_approval or action.action.casefold() in SENSITIVE_ACTIONS