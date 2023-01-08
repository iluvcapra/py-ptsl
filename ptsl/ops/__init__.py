from typing import Any

class Operation:
    """
    An operation composes a `CommandId` with its request and response type.

    The client runs `Operation`s with the Client.run() method. 
    """
    request: Any
    
    def command_id(self):
        assert False, "Required implementation missing"

    def response_body_prototype(self) -> Any:
        return None

    def on_empty_response_body(self):
        pass

    def on_response_body(self, _):
        pass


