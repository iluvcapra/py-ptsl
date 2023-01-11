from typing import List
import json

from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

class GetTrackList(Operation):
    
    def __init__(self, **kwargs) -> None:
        self.track_list : List[pt.Track] = []
        super().__init__(**kwargs)

    # FIXME: There is a bug here in the host's response JSON: when there are no
    # tracks, the response contains an empty dict in the "track_list" slot when
    # it should be returning an empty list
    def json_cleanup(self, in_json: str, ptsl_version) -> str:

        def empty_dict_to_empty_list(dct):
            if 'track_list' in dct and dct['track_list'] == {}:
                dct['track_list'] = []

            return dct

        decoded = json.loads(in_json, object_hook=empty_dict_to_empty_list)
        return json.dumps(decoded)


    def on_empty_response_body(self):
        self.track_list = []

    def on_response_body(self, body: pt.GetTrackListResponseBody):
        self.track_list.extend(body.track_list)




