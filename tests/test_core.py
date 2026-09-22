from orbisagents.core import *

def test_agents(): assert Coordinator([Agent("a",lambda x:x+1)]).run(2)==3
