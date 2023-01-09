from ptsl import PTSL_pb2 as pt

from ptsl.ops import Operation

    # # This does not work 
    # def create_session(self, name, session_location, 
    #     file_type : pt.FileType = pt.FT_WAVE, 
    #     sample_rate: pt.SampleRate = pt.SR_48000, 
    #     io_settings: pt.IOSettings = pt.IO_Last,
    #     is_interleaved = True,
    #     is_cloud_project = False,
    #     bit_depth: pt.BitDepth = pt.Bit24
    #     ):

    #     req_body = pt.CreateSessionRequestBody(session_name=name,file_type=file_type, sample_rate=sample_rate,
    #         input_output_settings=io_settings, is_interleaved=is_interleaved, 
    #         session_location=session_location, bit_depth=bit_depth, is_cloud_project=is_cloud_project)

    #     response = self._send_sync_request(pt.CreateSession, req_body)

    #     if response.header.status == pt.Failed:
    #         print("Failed:")
    #         print(response)


class CreateSession(Operation):

    request: pt.CreateSessionRequestBody

    def __init__(self, *args, **kwargs) -> None:
        self.request = pt.CreateSessionRequestBody(**kwargs)

    def command_id(self):
        return pt.CreateSession

    def on_empty_response_body(self):
        pass

    def on_response_body(self, _body):
        pass

