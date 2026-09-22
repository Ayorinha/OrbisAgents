from dataclasses import dataclass
@dataclass
class Agent: name:str; response:str
class RoundRobin:
 def __init__(self,agents): self.agents=agents
 def run(self,task): return [(a.name,a.response) for a in self.agents]
def consensus(results): return max(set(r for _,r in results),key=lambda r:sum(x==r for _,x in results))
