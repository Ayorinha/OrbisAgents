from orbisagents.core import RoundRobin,consensus
class A:
 def __init__(self,n,v): self.name=n; self.v=v
 def act(self,t): return self.v

def test_collaboration_and_consensus():
 r=RoundRobin([A("a","ok"),A("b","ok"),A("c","no")]).run("x")
 assert consensus(r)=="ok"
