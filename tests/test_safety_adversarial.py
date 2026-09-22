import pytest
from orbisagents.safety import AgentAction, requires_human_approval
def test_sensitive_action_is_case_insensitive(): assert requires_human_approval(AgentAction("agent", "DELETE"))
def test_missing_identity_fails_closed():
    with pytest.raises(ValueError): requires_human_approval(AgentAction("", "read"))
