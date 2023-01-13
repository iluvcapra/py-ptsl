import io
from contextlib import contextmanager
import json

from typing import Optional

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

    def __init__(self, api_key_path: str, address: str = 'localhost:31416') -> None:
        self.channel = grpc.insecure_channel(address)
        self.raw_client = PTSL_pb2_grpc.PTSLStub(self.channel) 
        self.session_id = ""
        if self._primitive_check_if_ready():
            self._primitive_authorize_connection(api_key_path)

        else:
            self.close()

    
    def run(self, operation: Operation, ptsl_version = None):
        """
        Run an operation on the client.

        :raises: `CommandError` if the server returns an error
        
        """
        request_body_json = self._prepare_operation_request_json(operation, ptsl_version)
        response = self._send_sync_request(operation.command_id(), request_body_json)
        operation.status = response.header.status
    
        if response.header.status == pt.Failed:
            # FIXME: Pro Tools returns a string error_type (instead of an int like it's
            # supposed to when you call SetSessionLength with a value less than 6 hours.
            # The error type it returns is "PT_InvalidParameter" which doesn't have a 
            # corresponding enum value.
            # print(response.response_error_json)
            cleaned_response_error_json = self._response_error_json_cleanup(response.response_error_json)
            # print(cleaned_response_error_json)
            command_error = json_format.Parse(cleaned_response_error_json, pt.CommandError())
            raise CommandError(command_error)

        elif response.header.status == pt.Completed:
            self._handle_completed_response(operation, ptsl_version, response)
        else:
            # FIXME: dump out for now, will be on the lookout for when this happens
            assert False, "Unexpected response code %i (%s)" % (response.header.status, 
                pt.TaskStatus.Name(response.header.status))


    def _response_error_json_cleanup(self, json_in: str) -> str:
        error_dict = json.loads(json_in)
        old_val = error_dict['command_error_type']
        if isinstance(old_val, str):
            if old_val.isdigit():
                error_dict['command_error_type'] = int(old_val)
            elif old_val in pt.CommandErrorType.keys():
                error_dict['command_error_type'] = pt.CommandErrorType.Value(old_val)
            else:
                error_dict['command_error_type'] = pt.PT_UnknownError

        return json.dumps(error_dict)


    # This is an in-progress feature 
    def launch_test_DO_NOT_USE(self, operation: Operation):
        request_body_json = self._prepare_operation_request_json(operation, self.ptsl_version)

        request = pt.Request(
            header=pt.RequestHeader(
                task_id="",
                session_id=self.session_id,
                command=operation.command_id(),
                version=PTSL_VERSION
            ),
            request_body_json=request_body_json
        )

        response_iter = self.raw_client.SendGrpcStreamingRequest(request)

        initial = next(response_iter)
        operation.task_id = initial.header.task_id

        return response_iter


    def _handle_completed_response(self, operation, ptsl_version, response):
        p = operation.__class__.response_body()
        if len(response.response_body_json) > 0 and p is not None:
            clean_json = operation.json_cleanup(response.response_body_json, ptsl_version or PTSL_VERSION)
            resp_body = json_format.Parse(clean_json, p(), ignore_unknown_fields=True)
            operation.on_response_body(resp_body)
        else:
            operation.on_empty_response_body()


    def _prepare_operation_request_json(self, operation, ptsl_version):
        if operation.request is None:
            request_body_json = ""
        else:
            request_body_json = json_format.MessageToJson(operation.request, 
                including_default_value_fields=True,
                preserving_proto_field_name=True)

        request_body_json = operation.json_messup(request_body_json, ptsl_version or PTSL_VERSION)
        return request_body_json


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


    def _primitive_authorize_connection(self, api_key_path) -> Optional[str]:
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
