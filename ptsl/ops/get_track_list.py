from typing import List

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetTrackList(Operation):

    request: pt.GetTrackListRequestBody
    track_list: List[pt.Track]

    def __init__(self, **kwargs) -> None:
        self.request = pt.GetTrackListRequestBody(**kwargs)
        self.track_list = []

    def command_id(self):
        return pt.GetTrackList

    def response_body_prototype(self):
        return pt.GetTrackListResponseBody()

    def on_empty_response_body(self):
        self.track_list = []

    def on_response_body(self, body: pt.GetTrackListResponseBody):
        self.track_list = body.track_list




