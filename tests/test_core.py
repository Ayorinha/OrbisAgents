from orbisagents.core import *
def test_consensus(): assert consensus(RoundRobin([Agent('a','ok'),Agent('b','ok')]).run('x'))=='ok'
