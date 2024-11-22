# toolshell.py

import cmd
import shlex
from typing import Optional

import ptsl
from ptsl import PTSL_pb2 as pt

class ToolShell(cmd.Cmd):
    intro = """
Toolshell is a demonstration command interpreter that 
can remotely operate Pro Tools. Type `help` or `?` to 
list commands.

To begin, type `connect`.
    """
    prompt = "(pt) "

    client = None

    def run_command_on_session(self, command_id: pt.CommandId, args: dict) -> Optional[dict]:
        if self.client is None:
            print("Command failed, not connected")
            return None

        try:
            r = self.client.run_command(command_id, args)
            return r
        except ptsl.errors.CommandError as e:
            if e.error_type == pt.PT_NoOpenedSession:
                print("command failed, no session is currently open")
                return None
        except:
            print("Command failed, Pro Tools may not be running")
            return None

    def do_connect(self, _):
        'Connect to Pro Tools'
        self.client = ptsl.client.Client(company_name="py-ptsl",
                                         application_name="Toolshell")
        if self.client is not None:
            self.prompt = f"(pt/connected) "

    def do_sinfo(self, _):
        'Print info about the open session: SINFO'
        r = self.run_command_on_session(pt.GetSessionName, {})

        assert r, "Failed to receive a response"
        session_name = r['session_name']
        r = self.run_command_on_session(pt.GetSessionIDs, {})        
        assert r
        print(f"Connected to Pro Tools session \"{session_name}\"")
        print(f"Session origin ID: {r['origin_id']}")
        print(f"Session instance ID: {r['instance_id']}")

    def do_newsession(self, args):
        'Create a new session: NEWSESSION name save-path sample-rate'
        name, path, sr = shlex.split(args)
        print(f"Creating new session {name} at {path} and SR {sr}")
        command_args = {'session_name': name,
                        'session_location': path,
                        'file_type': 'FT_WAVE',
                        'sample_rate': 'SR_' + str(sr),
                        'bit_depth': 'Bit24',
                        'input_output_settings': "IO_Last",
	 	                "is_interleaved": True,
	                    "is_cloud_project": False,
	                    "create_from_template": False,
	                    "template_group": "",
	                    "template_name": ""
                }
        assert self.client
        self.client.run_command(pt.CreateSession, command_args)

    def do_locate(self, args):
        'Locate to a given time in the current main counter format: LOCATE time'
        time = args.strip()
        command_args = {'play_start_marker_time': time,
                        'in_time': time,
                        'out_time': time,
                        }
        self.run_command_on_session(pt.SetTimelineSelection, command_args)

    def do_newmemloc(self, args):
        'Create a new marker memory location: NEWMEMLOC start-time'
        command_args = {'name': 'New Marker',
                        'start_time': args.strip(),
                        'end_time': args.strip(),
                        'time_properties': 'TP_Marker',
                        'reference': 'MLR_FollowTrackTimebase',
                        'general_properties': {
                            'zoom_settings': False,
                            'pre_post_roll_times': False,
                            'track_visibility': False,
                            'track_heights': False,
                            'group_enables': False,
                            'window_configuration': False,
                            },
                        'comments': "Created by toolshell",
                        'color_index': 1,
                        'location': 'MLC_MainRuler'
                            }
        
        self.run_command_on_session(pt.CreateMemoryLocation, command_args)

    def do_play(self, _):
        'Toggle the play state of the transport: PLAY'
        assert self.client
        try:
            self.client.run_command(pt.CommandId.TogglePlayState, {})
        except ptsl.errors.CommandError as e:
            if e.error_type == pt.PT_NoOpenedSession:
                print("play failed, no session is currently open")
                return False

    def do_bye(self, _):
        'Quit Toolshell and return to your shell: BYE'
        print("Tooshell quitting...")
        if self.client:
            self.client.close()
        return True


if __name__ == '__main__':
    ToolShell().cmdloop()
