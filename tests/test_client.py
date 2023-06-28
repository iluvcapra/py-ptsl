from __future__ import annotations
from typing import cast
from unittest import TestCase
from unittest.mock import patch

from google.protobuf import json_format

import ptsl.PTSL_pb2 as pt
from ptsl.client import open_client


class MockPtslStub:
    def __init__(self, session_id: str = "") -> None:
        self.session_id = session_id
        self.send_request_called = False
        self.register_connection_run = False

    def assert_send_request_called(self):
        assert self.send_request_called, \
            "SendGrpcRequest was not called"

    def assert_register_connection_run(self):
        assert self.register_connection_run, \
            "RegisterConnection command was not run"

    def SendGrpcRequest(
            self,
            request: pt.Request,
            _context=None) -> pt.Response:
        self.send_request_called = True
        response_body_json = None
        if request.header.command == pt.RegisterConnection:
            response_body_json = json_format.MessageToJson(
                pt.RegisterConnectionResponseBody(session_id=self.session_id)
            )
            self.register_connection_run = True

        return pt.Response(
            header=pt.ResponseHeader(
                task_id=request.header.task_id,
                command=request.header.command,
                status=pt.Completed,
                progress=100),
            response_body_json=response_body_json,
            response_error_json=None)


class TestClient(TestCase):

    def test_register_session(self):
        with patch('grpc.Channel'):
            with patch('ptsl.PTSL_pb2_grpc.PTSLStub') as stub:
                stub.return_value = MockPtslStub(session_id="abc123")

                with open_client(company_name='Test',
                                 application_name='Test') as client:

                    self.assertIsNotNone(client)
                    self.assertTrue(client.is_open)
                    self.assertEqual(client.session_id, "abc123")
                    cast(
                        MockPtslStub,
                        client.raw_client).assert_send_request_called()
                    cast(
                        MockPtslStub,
                        client.raw_client).assert_register_connection_run()
