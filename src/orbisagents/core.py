from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable
@dataclass(frozen=True, slots=True)
class Task: name: str; input: Any
@dataclass(frozen=True, slots=True)
class Agent:
    name: str; handler: Callable[[Any], Any]
    def execute(self, value: Any) -> Any: return self.handler(value)
class Coordinator:
    def __init__(self, agents: list[Agent]):
        if not agents or len({a.name for a in agents}) != len(agents): raise ValueError("agents must be non-empty and uniquely named")
        self.agents = tuple(agents)
    def run(self, value: Any) -> Any:
        for agent in self.agents: value = agent.execute(value)
        return value
