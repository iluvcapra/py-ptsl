#!/bin/sh

# build_proto.sh
#
# This script is used to generate the grpc and protobuf stub files.
# 
# To use:
# 1. Move the new PTSL.proto file to the ptsl/ directory.
# 2. Run the script.

set -x
python3 -m pip install grpcio
python3 -m pip install grpcio-tools
python3 -m grpc_tools.protoc --proto_path=ptsl PTSL.proto \
    --python_out=ptsl \
    --grpc_python_out=ptsl \
    --pyi_out=ptsl
sed -i '' -e 's/import PTSL_pb2 as PTSL__pb2/from . import PTSL_pb2 as PTSL__pb2/' \
    ptsl/PTSL_pb2_grpc.py

