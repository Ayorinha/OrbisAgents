from orbisagents.core import Agent, Coordinator

def test_sequential_agents():
    c = Coordinator([Agent("inc", lambda x: x + 1), Agent("double", lambda x: x * 2)])
    assert c.run(2) == 6

def test_duplicate_agents_rejected():
    try: Coordinator([Agent("a", lambda x: x), Agent("a", lambda x: x)])
    except ValueError: pass
    else: raise AssertionError("duplicates accepted")
