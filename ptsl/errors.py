"""
ptsl Exceptions
"""

from typing import Optional, List

from ptsl.PTSL_pb2 import CommandError as CommandErrorResponse
from ptsl.PTSL_pb2 import CommandErrorType


class CommandError(RuntimeError):
    """
    A :class:`Exception` for :class:`CommandError` results
    """
    error_responses: List[CommandErrorResponse]

    def __init__(self, error_responses: List[CommandErrorResponse]) -> None:
        self.error_responses = error_responses
        super().__init__()

    def __str__(self) -> str:
        return super().__str__() + \
            f"ErrType {self.error_type}: {self.error_name} ({self.message})"

    @property
    def is_warning(self) -> bool:
        """
        `True` if command error message is marked as a warning.
        """
        return self.error_responses[0].is_warning

    @property
    def error_type(self) -> CommandErrorType:
        """
        :class:`ptsl.PTSL_pb2.CommandErrorType` enumeration value.
        """
        return self.error_responses[0].command_error_type

    @property
    def error_name(self) -> Optional[str]:
        """
        Error name, if available.
        """
        if self.error_type in CommandErrorType.values():
            return CommandErrorType.Name(self.error_type)

        return None

    @property
    def message(self) -> str:
        """
        Error message as returned by the client.
        """
        return self.error_responses[0].command_error_message
