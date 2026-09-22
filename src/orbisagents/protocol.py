"""Deterministic coordination protocol primitives."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Message:
    sender: str
    recipient: str
    content: str
    turn: int

def validate_message(message: Message) -> None:
    if not message.sender or not message.recipient:
        raise ValueError("sender and recipient are required")
    if message.turn < 0:
        raise ValueError("turn must be non-negative")
