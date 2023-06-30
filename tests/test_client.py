from __future__ import annotations
from typing import cast
from unittest import TestCase
from unittest.mock import patch

from google.protobuf import json_format

import ptsl.PTSL_pb2 as pt
from ptsl.client import Client
from ptsl.errors import CommandError
from ptsl.ops import GetTrackList, Copy, Paste


class MockPtslStub:
    """
    This is a mock of :class:`~ptsl.PTSL_pb2_grpc.PTSLStub` that has a canned
    implementation of `SendGrpcRequest`.

    - The `~ptsl.PTSL_pb2.RegisterConnection` action returns a successful,
      properly-formed `~ptsl.PTSL_pb2.Response` with a
      `~ptsl.PTSL_pb2.RegisterConnectionResponseBody`.

    - The `~ptsl.PTSL_pb2.GetTrackList` action returns a successful response
      with an empty track list.

    - The `~ptsl.PTSL_pb2.Copy` action returns a failed response with a well-
      formed error json.

    - The `~ptsl.PTSL_pb2.Paste` action returns a failed response with a
      malformed error json meant to trigger the client's cleanup machinery.
    """

    def __init__(self, session_id: str = "") -> None:
        self.session_id = session_id
        self.send_request_called = False
        self.register_connection_run = False
        self.get_track_list_called = False

    def assert_send_request_called(self):
        assert self.send_request_called, \
            "SendGrpcRequest was not called"

    def assert_register_connection_run(self):
        assert self.register_connection_run, \
            "RegisterConnection command was not run"

    def assert_get_track_list_called(self):
        assert self.get_track_list_called, \
            "GetTrackList command was not run"

    def SendGrpcRequest(
            self,
            request: pt.Request,
            _context=None) -> pt.Response:
        self.send_request_called = True
        response_body_json = None
        error_body_json = None
        status = None

        if request.header.command == pt.RegisterConnection:
            status = pt.Completed
            response_body_json = json_format.MessageToJson(
                pt.RegisterConnectionResponseBody(session_id=self.session_id)
            )
            self.register_connection_run = True
        elif request.header.command == pt.GetTrackList:
            status = pt.Completed
            self.get_track_list_called = True
            response_body_json = json_format.MessageToJson(
                pt.GetTrackListResponseBody(
                    stats=pt.Pagination(
                        total=1,
                        limit=1,
                        offset=0),
                    track_list=[])
            )
        elif request.header.command == pt.Copy:
            status = pt.Failed
            error_body_json = json_format.MessageToJson(
                pt.CommandError(
                    command_error_type=pt.PT_UnknownError,
                    command_error_message="Test error response",
                    is_warning=False)
            )
        elif request.header.command == pt.Paste:
            status = pt.Failed
            error_body_json = """
            {
            "commandErrorType": "PT_CopyOptionCopy",
            "commandErrorMessage": "Test error message",
            "isWarning": true
            }
            """

        return pt.Response(
            header=pt.ResponseHeader(
                task_id=request.header.task_id,
                command=request.header.command,
                status=status,
                progress=100),
            response_body_json=response_body_json,
            response_error_json=error_body_json)


class TestClient(TestCase):

    def test_register_session(self):
        with patch('grpc.Channel'):
            with patch('ptsl.PTSL_pb2_grpc.PTSLStub') as stub:
                stub.return_value = MockPtslStub(session_id="abc123")

                client = Client(company_name='Test',
                                application_name='Test')

                self.assertIsNotNone(client)
                self.assertTrue(client.is_open)
                self.assertEqual(client.session_id, "abc123")
                cast(
                    MockPtslStub,
                    client.raw_client).assert_send_request_called()
                cast(
                    MockPtslStub,
                    client.raw_client).assert_register_connection_run()

                op = GetTrackList(page_limit=1,
                                  track_filter_list=[],
                                  is_filter_list_additive=True)

                client.run(op)
                tracks = op.track_list

                self.assertEqual(len(tracks), 0)

                op = Copy()
                with self.assertRaises(expected_exception=CommandError):
                    client.run(op)

                op = Paste()
                with self.assertRaises(expected_exception=CommandError):
                    client.run(op)

    # def test_run(self):
    #     with patch('grpc.Channel'):
    #         with patch('ptsl.PTSL_pb2_grpc.PTSLStub') as stub:
    #             stub.return_value = MockPtslStub()
    #
    #             client = Client(company_name='Test',
    #                              application_name='Test')
    #
    #             self.assertTrue(client.is_open)
