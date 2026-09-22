from dataclasses import dataclass
from collections import Counter

@dataclass(frozen=True)
class Vote:
    agent: str
    answer: str
    confidence: float = 1.0

def weighted_consensus(votes: list[Vote]) -> str:
    if not votes:
        raise ValueError("at least one vote is required")
    scores = Counter()
    for vote in votes:
        if not 0.0 <= vote.confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        scores[vote.answer] += vote.confidence
    return max(scores, key=scores.get)
