import pytest
from orbisagents.decision import Vote, weighted_consensus

def test_weighted_consensus():
    votes = [Vote("a", "yes", .9), Vote("b", "no", .2), Vote("c", "yes", .7)]
    assert weighted_consensus(votes) == "yes"

def test_invalid_confidence():
    with pytest.raises(ValueError):
        weighted_consensus([Vote("a", "yes", 2)])
