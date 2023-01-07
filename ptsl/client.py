import io

from typing import Optional

import grpc
from google.protobuf import json_format

from . import PTSL_pb2_grpc
from . import PTSL_pb2 as p

PTSL_VERSION=1

class Client:
    stub: grpc.Channel
    session_id: str

    def __init__(self, api_key_path, address = 'localhost:31416') -> None:
        channel = grpc.insecure_channel(address)
        self.stub = PTSL_pb2_grpc.PTSLStub(channel) 
        self.check_if_ready()
        self.authorize_connection(api_key_path)

    def check_if_ready(self):
        request = p.Request(
                header=p.RequestHeader(
                    task_id="", 
                    session_id="",
                    command=p.CommandId.HostReadyCheck,
                    version=PTSL_VERSION,
                    ), 
                request_body_json="")

        response = self.stub.SendGrpcRequest(request)
        if response.header.status == p.Failed:
            print("Pro Tools Not Ready")
            print(response)
        else:
            print("Pro Tools Ready")

    def authorize_connection(self, api_key_path) -> Optional[str]:
        with io.FileIO(api_key_path) as f:
            api_token = f.readall().decode(encoding='ascii')

        request = p.Request(
            header=p.RequestHeader(
                task_id="",
                session_id="",
                command=p.CommandId.AuthorizeConnection,
                version=PTSL_VERSION,
            ),
            request_body_json=json_format.MessageToJson(
                p.AuthorizeConnectionRequestBody(auth_string=api_token), 
                preserving_proto_field_name=True)
                )

        response : p.Response = self.stub.SendGrpcRequest(request)

        if response.header.status == p.Failed:
            print("An error occurred")
            print(response)
        else:
            authorization_response = json_format.Parse(response.response_body_json, p.AuthorizeConnectionResponseBody)
            if authorization_response.is_authorized:
                print("Connection authorized successfully, message:" + authorization_response.message)
                self.session_id = authorization_response.session_id
            else:
                print("Connection did not authorize, message: " + authorization_response.message)

            



# def run(api_key_path):
#     with grpc.insecure_channel('localhost:31416') as channel:
#         stub = PTSL_pb2_grpc.PTSLStub(channel)

#         check_if_ready(stub)
#         session_id = authorize_connection(stub, api_key_path)
#         print("Session ID is " + session_id)




