import grpc
import PTSL_pb2_grpc
from PTSL_pb2 import *

PTSL_VERSION=1

def run():
    with grpc.insecure_channel('localhost:0000') as channel:
        stub = PTSL_pb2_grpc.PTSLStub(channel)

        request = Request(
            header=RequestHeader(
                task_id="", 
                session_id="",
                command=CommandId.HostReadyCheck,
                version=PTSL_VERSION,
                ), 
            request_body_json="")

        response = stub.SendGrpcRequest(request)

        print(response)
