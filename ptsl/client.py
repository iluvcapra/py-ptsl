"""
ptsl Client
"""

import io
from contextlib import contextmanager
import json
import sys
import time

from typing import Optional

import grpc
from google.protobuf import json_format

from ptsl import PTSL_pb2_grpc
from ptsl import PTSL_pb2 as pt
from ptsl.errors import CommandError
from ptsl.ops import Operation

PTSL_VERSION = 1


@contextmanager
def open_client(*args, **kwargs):
    client = Client(*args, **kwargs)

    try:
        yield client
    finally:
        client.close()


class Auditor:
    """
    The Auditor is used by the client for reporting-out the status of requests
    as the are run.
    """

    def __init__(self, enabled: bool) -> None:
        self.output_stream = sys.stderr
        self.command_sn = 1
        self.enabled = enabled

    def emit(self, message):
        if self.enabled:
            time_str = time.strftime("[%Y-%m-%d %H:%M:%S]")
            print("%04i%s %s" % (self.command_sn, time_str, message),
                  file=self.output_stream)

    def run_called(self, command: pt.CommandId):
        self.emit(f"Started Command {pt.CommandId.Name(command)} " +
                  "({command})")

    def request_json_before_cleanup(self, json_data):
        self.emit(f"Created JSON for request message: {json_data}")

    def request_json_after_cleanup(self, json_data):
        self.emit(f"Re-formatted JSON for request message: {json_data}")

    def response_json_before_cleanup(self, json_data):
        self.emit(f"Received JSON response body: {json_data}")

    def response_json_after_cleanup(self, json_data):
        self.emit(f"Re-formatted JSON response body: {json_data}")

    def response_was_empty(self):
        self.emit("Received empty JSON response")

    def run_returning(self):
        self.emit("Finished Command")
        self.emit(f"{('*' * 60)}\n\n")
        self.command_sn += 1


class Client:
    """
    The Client class
        - maintains the grpc stub and channel
        - holds PTSL server session data
        - manages the connection's registration
        - runs `Operation`s on the grpc channel
        - packages error responses as exceptions to be thrown.
    """

    channel: grpc.Channel
    raw_client: PTSL_pb2_grpc.PTSLStub
    session_id: str
    auditor: Auditor
    is_open: bool

    def __init__(self, 
                 company_name: str, 
                 application_name: str,
                 address: str = 'localhost:31416') -> None:

        self.channel = grpc.insecure_channel(address)
        self.raw_client = PTSL_pb2_grpc.PTSLStub(self.channel)
        self.session_id = ""
        self.auditor = Auditor(enabled=False)

        try:
            self._primitive_check_if_ready()
            self._primitive_register_connection(company_name, application_name)
            self.is_open = True

        except grpc.RpcError as grpc_error:
            self.close()
            if getattr(grpc_error, 'code')() == grpc.StatusCode.UNAVAILABLE:
                print("gRPC endpoint was unavailable, Pro Tools " +
                      "may not be running.", file=sys.stderr)

            raise grpc_error

    def run(self, operation: Operation):
        """
        Run an operation on the client.

        :raises: `CommandError` if the server returns an error
        """
        self.auditor.run_called(operation.command_id())
        request_body_json = self._prepare_operation_request_json(operation)
        response = self._send_sync_request(operation.command_id(),
                                           request_body_json)
        operation.status = response.header.status

        if response.header.status == pt.Failed:
            cleaned_response_error_json = self._response_error_json_cleanup(
                response.response_error_json)
            command_error = json_format.Parse(cleaned_response_error_json,
                                              pt.CommandError())
            raise CommandError(command_error)

        elif response.header.status == pt.Completed:
            self._handle_completed_response(operation, response)
        else:
            # FIXME: dump out for now, will be on the lookout for when
            # this happens
            assert False, \
                f"Unexpected response code {response.header.status} " + \
                "({pt.TaskStatus.Name(response.header.status)})"

        self.auditor.run_returning()

    def _prepare_operation_request_json(self, operation):
        if operation.request is None:
            request_body_json = ""
        else:
            request_body_json = \
                json_format.MessageToJson(operation.request,
                                          including_default_value_fields=True,
                                          preserving_proto_field_name=True)

        self.auditor.request_json_before_cleanup(request_body_json)
        request_body_json = operation.json_messup(request_body_json)
        self.auditor.request_json_after_cleanup(request_body_json)
        return request_body_json

    def _response_error_json_cleanup(self, json_in: str) -> str:
        error_dict = json.loads(json_in)
        old_val = error_dict['command_error_type']
        if isinstance(old_val, str):
            if old_val.isdigit():
                error_dict['command_error_type'] = int(old_val)
            elif old_val in pt.CommandErrorType.keys():
                error_dict['command_error_type'] = \
                    pt.CommandErrorType.Value(old_val)
            else:
                error_dict['command_error_type'] = pt.PT_UnknownError

        return json.dumps(error_dict)

    def _handle_completed_response(self, operation, response):
        p = operation.__class__.response_body()
        if len(response.response_body_json) > 0 and p is not None:
            self.auditor.response_json_before_cleanup(
                response.response_body_json)

            clean_json = operation.json_cleanup(response.response_body_json)
            self.auditor.response_json_after_cleanup(clean_json)
            resp_body = json_format.Parse(clean_json, p(),
                                          ignore_unknown_fields=True)
            operation.on_response_body(resp_body)
        else:
            operation.on_empty_response_body()
            self.auditor.response_was_empty()

    def _send_sync_request(self, command_id,
                           request_body_json, task_id="") -> pt.Response:

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
        self.is_open = False
        self.channel.close()
        self.session_id = ""

    def _primitive_check_if_ready(self) -> bool:
        """
        Checks if the Pro Tools RPC server is listening. The server will
        respond to this command even if the client is not yet authenticated.
        """
        response = self._send_sync_request(pt.CommandId.HostReadyCheck, "")

        if response.header.status == pt.Failed:
            print("Pro Tools Not Ready")
            print(response)
            return False
        else:
            return True

    def _primitive_register_connection(self, company_name: str, 
                                       application_name: str):
        """
        Registers the client's connection to the Pro Tools RPC server.

        This method is called automatically by the initializer.
        """

        req = pt.RegisterConnectionRequestBody(company_name=company_name, 
                                               application_name=application_name)

        req_json = json_format.MessageToJson(req,
                                             preserving_proto_field_name=True)

        response = self._send_sync_request(pt.CommandId.RegisterConnection,
                                           req_json)

        if response.header.status == pt.Failed:
            print("An error occurred")
            print(response)
        else:
            registration_response = \
                json_format.Parse(response.response_body_json,
                                  pt.RegisterConnectionResponseBody)

            self.session_id = registration_response.session_id
                

