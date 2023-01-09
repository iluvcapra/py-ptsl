import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation


class CreateSession(Operation):

    request: pt.CreateSessionRequestBody

    def __init__(self, *args, **kwargs) -> None:
        self.request = pt.CreateSessionRequestBody(**kwargs)

    def command_id(self):
        return pt.CreateSession

    # FIXME: There's something wrong with the protobuf code here, it's simply
    # not capturing either is_cloud_project or create_from_template from the
    # creation call.
    # def json_messup(self, in_json: str, version=1) -> str:
    #     def hook(dct: dict):
    #         dct['is_cloud_project'] = False
    #         dct['create_from_template'] = False

    #         return dct

    #     transformed = json.loads(in_json, object_hook=hook)

    #     return json.dumps(transformed)


    def on_empty_response_body(self):
        pass


    def on_response_body(self, _body):
        pass

