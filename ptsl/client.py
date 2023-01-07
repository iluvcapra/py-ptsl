import grpc
from . import PTSL_pb2_grpc
from . import PTSL_pb2 as p

PTSL_VERSION=1

def run():
    with grpc.insecure_channel('localhost:0000') as channel:
        stub = PTSL_pb2_grpc.PTSLStub(channel)

        request = p.Request(
            header=p.RequestHeader(
                task_id="", 
                session_id="",
                command=p.CommandId.HostReadyCheck,
                version=PTSL_VERSION,
                ), 
            request_body_json="")

        print(request)

        #response = stub.SendGrpcRequest(request)

        #print(response)
