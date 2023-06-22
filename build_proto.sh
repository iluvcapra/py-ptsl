#!/bin/sh
set -x
python3 -m pip install grpcio
python3 -m pip install grpcio-tools
python3 -m grpc_tools.protoc --proto_path=ptsl PTSL.proto \
    --python_out=ptsl \
    --grpc_python_out=ptsl \
    --pyi_out=ptsl
sed -i '' -e 's/import PTSL_pb2 as PTSL__pb2/from . import PTSL_pb2 as PTSL__pb2/' \
    ptsl/PTSL_pb2_grpc.py

