from typing import Any

class Operation:
    request: Any
    
    def command_id(self):
        assert False, "Required implementation missing"

    def response_body_prototype(self) -> Any:
        return None

    def on_empty_response_body(self):
        pass

    def on_response_body(self, _):
        pass


