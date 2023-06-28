import json

from ptsl.ops import Operation


class GetSessionInterleavedState(Operation):

    # Reported https://duc.avid.com/showthread.php?t=423087
    #
    # Pro Tools is returning the "possible_settings" list as
    # a list of strings and not a list of bools
    def json_cleanup(self, in_json: str) -> str:
        decoder = json.decoder.JSONDecoder()
        parsed = decoder.decode(in_json)
        parsed["possible_settings"] = [True, False]
        encoder = json.encoder.JSONEncoder()
        return encoder.encode(parsed)
