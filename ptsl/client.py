import io

from typing import Optional

import grpc
from google.protobuf import json_format

from . import PTSL_pb2_grpc
from . import PTSL_pb2 as p

PTSL_VERSION=1

def run(api_key_path):
    with grpc.insecure_channel('localhost:31416') as channel:
        stub = PTSL_pb2_grpc.PTSLStub(channel)

        check_if_ready(stub)
        session_id = authorize_connection(stub, api_key_path)
        print("Session ID is " + session_id)


def authorize_connection(stub, api_key_path) -> Optional[str]:

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

    response : p.Response = stub.SendGrpcRequest(request)

    if response.header.status == p.Failed:
        print("An error occurred")
        print(response)
        return None
    else:
        authorization_response = json_format.Parse(response.response_body_json, p.AuthorizeConnectionResponseBody)
        if authorization_response.is_authorized:
            print("Connection authorized successfully, message:" + authorization_response.message)
            return authorization_response.session_id
        else:
            print("Connection did not authorize, message: " + authorization_response.message)
            return None
        


def check_if_ready(stub):
    request = p.Request(
            header=p.RequestHeader(
                task_id="", 
                session_id="",
                command=p.CommandId.HostReadyCheck,
                version=PTSL_VERSION,
                ), 
            request_body_json="")

    response = stub.SendGrpcRequest(request)
    if response.header.status == p.Failed:
        print("Pro Tools Not Ready")
        print(response)
    else:
        print("Pro Tools Ready")
