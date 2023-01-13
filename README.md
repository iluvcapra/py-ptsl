# py-ptsl

Native Python client for the Pro Tools scripting RPC interface

## Work In Progress

This project is in an early phases of developmen. The 
client successfully connects to Pro Tools, will authorize your connection with your
developer key and a few commands are exposed through the `Engine` interface. PRs and issue submissions are welcome
to guide future development!

## Example

See the [examples directory](examples) for scripts demonstrating how to use the client.

### Sending Commands To Pro Tools with the `Engine` class

The `Engine` class exposes `ptsl` commands with a method call interface.

```python
from ptsl import open_engine

with open_engine(api_key_path) as engine:
    session_name = engine.session_name()

```

_Note:_ A PTSL connection to Pro Tools must be authorized with a developer 
certificate, this is handled automatically by the client, you just need to
provide a path to your developer cert to `open_engine()`. All of the scripts
in the examples folder will look for this in the `PTSL_KEY` environment 
variable, you should set and export this variable to a path to your certificate 
json file. For example in the fish shell you would do this with `set`...

```fish
set -Ux PTSL_KEY /path/to/your/cert.json
```

### Script: [session_info.py](examples/session_info.py)

This script will print a list of gettable properties from the currently open session.

_Note:_ All of the examples in the examples directory look at the `PTSL_KEY` environment
variable to get a path to your PTSL developer key file.


```sh
$ python3 examples/session_info.py
PTSL Version: 1
Session Name: New Session
Session Path: Macintosh HD:Users:jamie:New Session:New Session.ptx
Session Sample Rate: 96000
Session Audio Format: WAVE
Session Audio Interlaved: TRUE
Session Timecode Rate: 29.970 Non-Drop
Session Start Time: 00:57:03:16.00
Session Length: 24:00:00:00
Session feet+frames rate: 23.976
-------------------------------
Transport State: TS_TransportStopped 
Transport Arm: SAFE
Playback Modes: Loop
Record Mode: RM_Normal
```


### Script: [print_tracks.py](examples/print_tracks.py)

This script will print a list of every track in the currently open session.

```sh
$  python3 examples/print_tracks.py
#: ATTRS : TYPE          : NAME                             :     COLOR : ID
1: *     : RoutingFolder : Folder 2                         : #ff2a2a2a : {00000000-2a000000-f404e1df-f298fd4b}
2: *S    : AudioTrack    : A1                               : #ff2a2a2a : {00000000-2a000000-d4cbe0df-2590e43e}
3: *     : AudioTrack    : A2                               : #ff2a2a2a : {00000000-2a000000-d4cbe0df-ac40203f}
4:       : BasicFolder   : Folder 1                         : #ff2a2a2a : {00000000-2a000000-de01e1df-2d2b4575}
5:  SM   : Vca           : VCA 1                            : #ffbc1e0d : {00000000-2a000000-a301e1df-f690ac51}
6:       : Vca           : VCA 2                            : #ffbc1e0d : {00000000-2a000000-a301e1df-5b0aad51}
7:       : AudioTrack    : B1                               : #ff2a2a2a : {00000000-2a000000-d4cbe0df-d3ae273f}
8:    HX : AudioTrack    : B2                               : #ff2a2a2a : {00000000-2a000000-d4cbe0df-cc3b283f}
```
