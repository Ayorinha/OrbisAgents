from orbisagents.safety import AgentAction,requires_human_approval

def test_consequential_action_requires_approval():
    assert requires_human_approval(AgentAction("a","publish"))
