from typing import Optional

from . import PTSL_pb2 as pt

class CommandError(RuntimeError):
    error_response: pt.CommandError

    def __init__(self, error_response: pt.CommandError) -> None:
        self.error_response = error_response
        super().__init__()

    @property
    def is_warning(self) -> bool:
        return self.error_response.is_warning

    @property
    def error_type(self) -> pt.CommandErrorType:
        return self.error_response.command_error_type

    @property
    def error_name(self) -> Optional[str]:
        if self.error_type in pt.CommandErrorType.values():
            return pt.CommandErrorType.Name(self.error_type)
        else:
            return None

    @property
    def message(self) -> str:
        return self.error_response.command_error_message