import io
from contextlib import contextmanager

from typing import Optional, List

import grpc
from google.protobuf import json_format

from . import PTSL_pb2_grpc
from . import PTSL_pb2 as pt

from .ops import Operation, GetPTSLVersion

PTSL_VERSION=1

class CommandError(RuntimeError):
    error_response: pt.CommandError

    def __init__(self, error_response: pt.CommandError) -> None:
        self.error_response = error_response
        super().__init__()


@contextmanager
def open_client(*args, **kwargs):
    client = Client(*args, **kwargs)

    try:
        yield client
    finally:
        client.close()


class Client:
    channel: grpc.Channel
    raw_client: PTSL_pb2_grpc.PTSLStub
    session_id: str
    ptsl_version: int

    def __init__(self, api_key_path: str, address: str = 'localhost:31416') -> None:
        self.channel = grpc.insecure_channel(address)
        self.raw_client = PTSL_pb2_grpc.PTSLStub(self.channel) 
        self.session_id = ""
        if self._primitive_check_if_ready():
            self._authorize_connection(api_key_path)
            get_v = GetPTSLVersion()
            self.run(get_v, ptsl_version=1)
            self.ptsl_version = get_v.response.version
        else:
            self.close()


    def run(self, operation: Operation, ptsl_version = None):
        """
        Run an operation on the client.

        :raises: `CommandError` if the server returns an error
        
        """
        if operation.request is None:
            request_body_json = ""
        else:
            request_body_json = json_format.MessageToJson(operation.request, 
                including_default_value_fields=True,
                preserving_proto_field_name=True)

        request_body_json = operation.json_messup(request_body_json, ptsl_version or self.ptsl_version)
        
        response = self._send_sync_request(operation.COMMAND_ID, request_body_json)

        operation.status = response.header.status

        if response.header.status == pt.Failed:
            command_error = json_format.Parse(response.response_error_json, pt.CommandError())
            self._default_error_handler(operation, command_error)
            raise CommandError(command_error)

        elif response.header.status == pt.Completed:
            p = operation.RESPONSE_BODY
            if len(response.response_body_json) > 0 and p is not None:
                clean_json = operation.json_cleanup(response.response_body_json, ptsl_version or self.ptsl_version)
                resp_body = json_format.Parse(clean_json, p(), ignore_unknown_fields=True)
                operation.on_response_body(resp_body)
            else:
                operation.on_empty_response_body()

            return None
        else:
            # FIXME: dump out for now, will be on the lookout for when this happens
            assert False, "Unexpected response code %i (%s)" % (response.header.status, 
                pt.TaskStatus.Name(response.header.status))

    def _send_sync_request(self, command_id, request_body_json, task_id="") -> pt.Response:
        request = pt.Request(
            header=pt.RequestHeader(
                task_id=task_id,
                session_id=self.session_id,
                command=command_id,
                version=PTSL_VERSION
            ),
            request_body_json=request_body_json
        )

        response = self.raw_client.SendGrpcRequest(request)

        return response


    def _default_error_handler(self, operation: Operation, command_error: pt.CommandError):
        error_type = "WARNING" if command_error.is_warning else "FAILURE"

        message = "%s: Operation %s failed.\n  Error type %i (%s)\n  Message: %s" % (error_type, 
                pt.CommandId.Name(operation.command_id()),
                command_error.command_error_type,
                pt.CommandErrorType.Name(command_error.command_error_type),
                command_error.command_error_message )

        print(message)


    def close(self):
        """
        Closes the client.
        """
        self.raw_client = None
        self.channel.close()
        self.session_id = ""


    # This works
    def _primitive_check_if_ready(self) -> bool:
        """
        Checks if the Pro Tools RPC server is listening. The server will respond
        to this command even if the client is not yet authenticated.
        """
        response = self._send_sync_request(pt.CommandId.HostReadyCheck, "")

        if response.header.status == pt.Failed:
            print("Pro Tools Not Ready")
            print(response)
            return False
        else:
            return True


    def _authorize_connection(self, api_key_path) -> Optional[str]:
        """
        Authorizes the client's connection to the Pro Tools RPC server.

        This method is called automatically by the initializer.
        """
        KEY_FILE_ENCODING = 'ascii'

        with io.FileIO(api_key_path) as f:
            api_token = f.readall().decode(encoding=KEY_FILE_ENCODING)
        
        req = pt.AuthorizeConnectionRequestBody(auth_string=api_token)
        req_json = json_format.MessageToJson(req, preserving_proto_field_name=True) 
        response = self._send_sync_request(pt.CommandId.AuthorizeConnection, req_json)

        if response.header.status == pt.Failed:
            print("An error occurred")
            print(response)
        else:
            authorization_response = json_format.Parse(response.response_body_json, pt.AuthorizeConnectionResponseBody)
            if authorization_response.is_authorized:
                # print("Connection authorized successfully, message:" + authorization_response.message)
                self.session_id = authorization_response.session_id
            else:
                print("Connection did not authorize, message: " + authorization_response.message)
