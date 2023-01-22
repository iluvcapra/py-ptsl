from typing import Optional

from ptsl.PTSL_pb2 import CommandError, CommandErrorType


class CommandError(RuntimeError):
    error_response: CommandError

    def __init__(self, error_response: CommandError) -> None:
        self.error_response = error_response
        super().__init__()

    def __str__(self) -> str:
        return super().__str__() + \
            ("ErrType %i: %s (%s)" % (self.error_type,
                                      self.error_name,
                                      self.message))

    @property
    def is_warning(self) -> bool:
        return self.error_response.is_warning

    @property
    def error_type(self) -> CommandErrorType:
        return self.error_response.command_error_type

    @property
    def error_name(self) -> Optional[str]:
        if self.error_type in CommandErrorType.values():
            return CommandErrorType.Name(self.error_type)
        else:
            return None

    @property
    def message(self) -> str:
        return self.error_response.command_error_message
