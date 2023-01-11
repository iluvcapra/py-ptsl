# py-ptsl

Native Python client for the Pro Tools scripting RPC interface

## Work In Progress

This project is in an early phases of developmen. The 
client successfully connects to Pro Tools, will authorize your connection with your
developer key and a few commands are exposed through the `Engine` interface. PRs and issue submissions are welcome
to guide future development!

## Example

See the examples directory for scripts demonstrating how to use the client.

### session_info.py

This script will print a list of gettable properties from the currently open session.

```sh
$ python3 examples/session_info.py '/path/to/<your api key>.json'  
PTSL Version: 1
Session Name: Untitled
Session Path: Macintosh HD:Users:jamiehardt:Desktop:Untitled:Untitled.ptx
Session Sample Rate: SR_48000
Session Audio Format: FT_WAVE
Session Interleaved: TRUE
Session Timecode Rate: STCR_Fps23976
Session Start Time: 00:57:00:00.00
Session Length: 24:00:00:00
Session Feet+Frames Rate: SFFR_Fps23976
Session Audio Pull Setting: SRP_None
Session Video Pull Setting: SRP_None
Transport State: TS_TransportStopped
Transport Armed: FALSE
Playback Modes: PM_Normal
Record Mode: RM_Normal
```
### print_tracks.py

This script will print a list of every track in the currently open session.

```sh
$  python3  examples/print_tracks.py '/path/to/<your api key>.json' 
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
