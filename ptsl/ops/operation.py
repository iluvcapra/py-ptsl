from typing import TypeVar, Optional

from ptsl import PTSL_pb2 as pt



class Operation:
    """
    An operation composes a `CommandId` with its request and response type.

    The client runs `Operation`s with the Client.run() method. 
    """

    @classmethod
    def request_body(cls):
        return getattr(pt, cls.__name__ + "RequestBody", None)

    @classmethod
    def response_body(cls):
        return getattr(pt, cls.__name__ + "ResponseBody", None)

    @classmethod
    def command_id(cls):
        return getattr(pt, cls.__name__, -1)


    def __init__(self, *args, **kwargs) -> None:
        rq = self.__class__.request_body()
        if rq:
            self.request = rq(**kwargs)
        else:
            self.request = None
        
        self.response = None
        self.status = None

    def json_messup(self, in_json: str, version = 1) -> str:
        """
        A shim to adapt the json the Protobuf machinery creates into what Pro Tools
        expects. Necessary if the server's request parser is buggy/not doing what 
        the .proto file says it should

        :param in_json: json for the RequestBody that the Protobuf code generated
        :returns: the json that will be used for the RequestBody sent to Pro Tools.
        """
        return in_json

    def json_cleanup(self, in_json: str, version = 1) -> str:
        """
        A shim to adapt the json Pro Tools generates in response to what Protobuf expects. 
        Necessary if the Pro Tools response JSON is buggy/not doing what 
        the .proto file says it should. (Happens sometimes!)

        :param in_json: json from the ResponseBody Pro Tools sent.
        :returns: the json that will be passed to Protobuf.
        """
        return in_json

    def on_empty_response_body(self):
        """
        The client calls this when the server reponds.
        """
        pass

    def on_response_body(self, response_body):
        """
        The client calls this when the server responds with a JSON `pt.ResponseBody`.
        """
        self.response = response_body