# py-ptsl

Native Python client for the Pro Tools scripting RPC interface

## Work In Progress

This project is in an early phases of development. The 
client successfully connects to Pro Tools, will authorize your connection with your
developer key and about half of the available commands are exposed through the `Engine` interface. PRs and issue submissions are welcome
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
certificate, this process is handled automatically by the client at on opening.
By default the `Engine` class will look for a path to your developer 
certificate in the `PTSL_KEY` environment variable. You should set this in your
shell, for example in the fish shell...

```fish
set -Ux PTSL_KEY /path/to/your/cert.json
```

### Script: [session_info.py](examples/session_info.py)

This script will print a list of gettable properties from the currently open session.

```sh
$ python3 examples/session_info.py
PTSL Version: 1
Session Name: Test2
Session Path: Macintosh HD:Users:jamie:Test2:Test2.ptx
Session Sample Rate: 48000
Session Audio Format: SAF_WAVE
Session Bit Depth: Bit24
Session Audio Interlaved: TRUE
Session Timecode Rate: STCR_Fps2997
Session Start Time: 01:58:00:00.00
Session Length: 20:00:00:00
Session feet+frames rate: SFFR_Fps23976
Session Audio Rate Pull: SRP_None
Session Video Rate Pull: SRP_None
-------------------------------
Transport State: TS_TransportStopped 
Transport Arm: SAFE
Playback Modes: Normal
Record Mode: RM_Loop
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
