from typing import Any

class Operation:
    """
    An operation composes a `CommandId` with its request and response type.

    The client runs `Operation`s with the Client.run() method. 
    """
    request: Any
    
    def __init__(self) -> None:
        self.request = None

    def command_id(self):
        return -1

    def response_body_prototype(self) -> Any:
        return None

    def on_empty_response_body(self):
        pass

    def on_response_body(self, _):
        pass