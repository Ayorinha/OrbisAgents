from orbisagents.protocol import Message, validate_message

def test_message_validation(): validate_message(Message("a","b","hello",0))
