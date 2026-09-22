from dataclasses import dataclass
from typing import Any,Callable
@dataclass(frozen=True)
class Task: name:str; input:Any
@dataclass
class Agent:
 name:str; handler:Callable[[Any],Any]
 def execute(self,value):return self.handler(value)
class Coordinator:
 def __init__(self,agents):
  if not agents:raise ValueError("at least one agent is required")
  self.agents=agents
 def run(self,value):
  for agent in self.agents:value=agent.execute(value)
  return value
