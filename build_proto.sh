#!/bin/sh
set -x
python3 -m pip install grpcio
python3 -m pip install grpcio-tools
python3 -m grpc_tools.protoc --proto_path=ptsl PTSL.proto \
    --python_out=ptsl \
    --grpc_python_out=ptsl \
    --pyi_out=ptsl

