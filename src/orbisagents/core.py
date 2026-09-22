from dataclasses import dataclass
from typing import Protocol

class Agent(Protocol):
    name:str
    def act(self, task:str)->str: ...

@dataclass
class RoundRobin:
    agents:list[Agent]
    def run(self, task:str)->list[tuple[str,str]]:
        return [(a.name,a.act(task)) for a in self.agents]

def consensus(results:list[tuple[str,str]])->str:
    if not results: raise ValueError("no agent results")
    counts={r:sum(x[1]==r for x in results) for r in results}
    return max(counts,key=counts.get)
