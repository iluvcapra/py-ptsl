# from typing import Optional
# import mock
#
# import grpc
#
# from google.protobuf import json_format
#
# from ptsl.PTSL_pb2 import Response, ResponseHeader, GetPTSLVersion, \
#     Completed, GetPTSLVersionResponseBody
# from ptsl.engine import Engine, open_engine
# from ptsl.client import Client
# import ptsl.ops as ops
#
#
# def test_get_version():
#     mock_client = mock.create_autospec(Client)
#     rval = ops.GetPTSLVersion()
#     rval.response = Response(
#             header=ResponseHeader(task_id=None,
#                                   command=GetPTSLVersion,
#                                   status=Completed,
#                                   progress=100),
#             response_body_json=json_format.MessageToJson(
#                 GetPTSLVersionResponseBody(version=1))
#             )
#
#     mock_client.run = mock.Mock(
#         return_value=rval
#     )
#     
#     with open_engine(client=mock_client) as engine:
#         engine.ptsl_version()
#         mock_client.run.assert_called()
