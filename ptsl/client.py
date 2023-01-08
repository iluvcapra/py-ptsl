import io

from typing import Optional, List

import grpc
from google.protobuf import json_format

from . import PTSL_pb2_grpc
from . import PTSL_pb2 as pt

from .ops import Operation

PTSL_VERSION=1

class Client:
    channel: grpc.Channel
    raw_client: PTSL_pb2_grpc.PTSLStub
    session_id: str


    def __init__(self, api_key_path: str, address: str = 'localhost:31416') -> None:
        self.channel = grpc.insecure_channel(address)
        self.raw_client = PTSL_pb2_grpc.PTSLStub(self.channel) 
        self.session_id = ""
        if self._primitive_check_if_ready():
            self._authorize_connection(api_key_path)


    def _send_sync_request(self, command_id, request_body, task_id="") -> pt.Response:
        if request_body is not None:
            request_body_json = json_format.MessageToJson(request_body, preserving_proto_field_name=True)
        else:
            request_body_json = "" 

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


    def run(self, operation: Operation) -> Optional[pt.CommandError]:
        """
        Run an operation on the client.

        :returns: If the response from the server is 
        """
        response = self._send_sync_request(operation.command_id, operation.request)

        if response.header.status == pt.Failed:
            command_error = json_format.Parse(response.response_error_json, pt.CommandError())
            self.error_handler(operation, command_error)
            return command_error

        elif response.header.status == pt.Completed:
            p = operation.response_body_prototype
            if len(response.response_body_json) > 0 and p is not None:
                resp_body = json_format.Parse(response.response_body_json, p, ignore_unknown_fields=True)
                operation.on_response_body(resp_body)
            else:
                operation.on_empty_response_body()

            return None
        else:
            # FIXME: dump out for now, will be on the lookout for when this happens
            assert False, "Unexpected response code %i (%s)" % (response.header.status, 
                pt.TaskStatus.Name[response.header.status])


    def error_handler(self, operation: Operation, command_error: pt.CommandError):
        error_type = "WARNING" if command_error.is_warning else "FAILURE"

        message = "%s: Operation %s failed.\n  Error type %i (%s)\n  Message: %s" % (error_type, 
                pt.CommandId.Name[operation.command_id],
                command_error.command_error_type,
                pt.CommandErrorType.Name[command_error.command_error_type],
                command_error )

        print(message)

    def close(self):
        """
        Closes the client.
        """
        self.raw_client = None
        self.channel.close()
        self.session_id = ""

    # This works
    def get_session_sample_rate(self) -> pt.SampleRate:
        response = self._send_sync_request(pt.CommandId.GetSessionSampleRate, None)

        if response.header.status == pt.Failed:
            print("Failed:")
            print(response)
        else:
            body = json_format.Parse(response.response_body_json, pt.GetSessionSampleRateResponseBody(), 
                ignore_unknown_fields=True)
            return body.sample_rate

    # This works
    def get_session_audio_format(self) -> pt.FileType:
        response = self._send_sync_request(pt.GetSessionAudioFormat, None)

        if response.header.status == pt.Failed:
            print("Failed:")
            print(response)
        else:
            body = json_format.Parse(response.response_body_json, pt.GetSessionAudioFormatResponseBody())
            return body.current_setting

    # This does not work 
    # Here is the error I get: https://gist.github.com/iluvcapra/fb8e2480070b0a9891076d39ed95d605
    def create_session(self, name, session_location, 
        file_type : pt.FileType = pt.FT_WAVE, 
        sample_rate: pt.SampleRate = pt.SR_48000, 
        io_settings: pt.IOSettings = pt.IO_Last,
        is_interleaved = True,
        is_cloud_project = False,
        bit_depth: pt.BitDepth = pt.Bit24
        ):

        req_body = pt.CreateSessionRequestBody(session_name=name,file_type=file_type, sample_rate=sample_rate,
            input_output_settings=io_settings, is_interleaved=is_interleaved, 
            session_location=session_location, bit_depth=bit_depth, is_cloud_project=is_cloud_project)

        response = self._send_sync_request(pt.CreateSession, req_body)

        if response.header.status == pt.Failed:
            print("Failed:")
            print(response)

    # This fails if there are zero tracks, the JSON returned from Pro Tools in the response
    # body has a strange format
    #
    # Here is the error I get: https://gist.github.com/iluvcapra/90601ade487b245510e08b9c68650925
    def get_track_list(self, filters : List[pt.TrackListInvertibleFilter] = 
            [pt.TrackListInvertibleFilter(filter=pt.All, is_inverted=False)]):

        req_body = pt.GetTrackListRequestBody(page_limit=24, 
            track_filter_list=filters, 
            is_filter_list_additive=False)

        response = self._send_sync_request(pt.GetTrackList, req_body)

        if response.header.status == pt.Failed:
            print("Failed:")
            print(response)
        else:
            resp_body = json_format.Parse(response.response_body_json, pt.GetTrackListResponseBody())
            return resp_body.track_list

    # This works
    def _primitive_check_if_ready(self) -> bool:
        """
        Checks if the Pro Tools RPC server is listening. The server will respond
        to this command even if the client is not yet authenticated.
        """
        response = self._send_sync_request(pt.CommandId.HostReadyCheck, None)

        if response.header.status == pt.Failed:
            print("Pro Tools Not Ready")
            print(response)
            return False
        else:
            return True

    # This works
    def _authorize_connection(self, api_key_path) -> Optional[str]:
        """
        Authorizes the client's connection to the Pro Tools RPC server.

        This method is called automatically by the initializer.
        """
        KEY_FILE_ENCODING = 'ascii'

        with io.FileIO(api_key_path) as f:
            api_token = f.readall().decode(encoding=KEY_FILE_ENCODING)

        response = self._send_sync_request(pt.CommandId.AuthorizeConnection, pt.AuthorizeConnectionRequestBody(auth_string=api_token))

        if response.header.status == pt.Failed:
            print("An error occurred")
            print(response)
        else:
            authorization_response = json_format.Parse(response.response_body_json, pt.AuthorizeConnectionResponseBody)
            if authorization_response.is_authorized:
                print("Connection authorized successfully, message:" + authorization_response.message)
                self.session_id = authorization_response.session_id
            else:
                print("Connection did not authorize, message: " + authorization_response.message)
