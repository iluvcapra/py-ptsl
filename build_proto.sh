#!/bin/sh

# thus from https://grpc.io

python3 -m pip install --upgrade pip
python3 -m pip install grpcio
python3 -m pip install grpcio-tools

python3 -m grpc_tools.protoc --proto_path=. ./unary.proto --python_out=. --grpc_python_out=.
