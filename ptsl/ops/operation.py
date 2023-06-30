from typing import TypeVar, Generic

from ptsl import PTSL_pb2 as pt

Q = TypeVar("Q")
R = TypeVar("R")


class Operation(Generic[Q, R]):
    """
    An operation composes a `CommandId` with its request and response type.
    The `Operation` abstract base class will infer the `CommandId` Request
    and Response type from the class name, and will look up the command ID
    code number based on its class name. These can be overridden in subclasses
    for special cases but most of the time simply naming a class after its
    CommandId enum name and deriving it from `Operation` will be sufficient.

    The client runs `Operation`s with the Client.run() method.
    """
    request: Q
    response: R

    @classmethod
    def request_body(cls) -> Q:
        return getattr(pt, cls.__name__ + "RequestBody", None)  # type: ignore

    @classmethod
    def response_body(cls) -> R:
        return getattr(pt, cls.__name__ + "ResponseBody", None)  # type: ignore

    @classmethod
    def command_id(cls):
        return getattr(pt, cls.__name__, -1)

    def __init__(self, *args, **kwargs) -> None:
        rq = self.__class__.request_body()
        if rq is not None:
            self.request = rq(**kwargs)  # type: ignore
        else:
            self.request = None  # type: ignore

        self.response = None  # type: ignore
        self.status = None
        self.task_id = ""

    def json_messup(self, in_json: str) -> str:
        """
        A shim that can be overriden by subclasses to adapt the json the
        Protobuf machinery creates into what Pro Tools expects. Necessary
        if the server's request parser is buggy/not doing what the .proto
        file says it should

        :param in_json: json from protobuf's `MessageToJson` method
        :returns: json to be used in the operation's request_body
        """
        return in_json

    def json_cleanup(self, in_json: str) -> str:
        """
        A shim that can be overriden by subclases to adapt the json Pro
        Tools generates in response to what Protobuf expects. Necessary if
        the Pro Tools response JSON is buggy/not doing what the .proto file
        says it should. (Happens sometimes!)

        :param in_json: json from the ResponseBody Pro Tools sent.
        :returns: the json that will be passed to Protobuf's
        `json_format.Parse` method.
        """
        return in_json

    def on_empty_response_body(self):
        """
        The client calls this when the server reponds.
        """
        self.response = None  # type: ignore

    def on_response_body(self, response_body: R):
        """
        The client calls this when the server responds with a JSON
        `pt.ResponseBody`.
        """
        self.response = response_body
