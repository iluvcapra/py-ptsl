# py-ptsl

Native Python client for the Pro Tools scripting RPC interface

## Work In Progress

This project is in the very early phases of development (almost nothing works). The 
client successfully connects to Pro Tools, will authorize your connection with your
developer key and a few commands are exposed. PRs and issue submissions are welcome
to guide future development!

## Example

See the examples directory for scripts demonstrating how to use the client.

### session_info.py

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

```python

import ptsl.client

c = ptsl.client.Client("path/to/<your api key>.json")

track_list = c.get_track_list()
```

## API Coverage

|Command| Implemented | Notes |
| ----- | :---------: | ----- |
|CreateSession| |
|OpenSession|  |
|Import|  |
|GetTrackList| ☑️ |
|SelectAllClipsOnTrack|  |
|ExtendSelectionToTargetTracks|   |
|TrimToSelection|  |
|CreateFadesBasedOnPreset|  |
|RenameTargetTrack|  |
|ConsolidateClip|  |
|ExportClipsAsFiles|  |
|ExportSelectedTracksAsAAFOMF|  |
|GetTaskStatus|  |
|HostReadyCheck| ☑️ |
|RefreshTargetAudioFiles|  |
|RefreshAllModifiedAudioFiles|   |
|GetFileLocation|  |
|CloseSession|  |
|SaveSession|  |
|SaveSessionAs|  |
|Cut|  |
|Copy|  |
|Paste|  |
|Clear|  |
|CutSpecial|  |
|CopySpecial|  |
|ClearSpecial|  |
|PasteSpecial|  |
|ExportMix|  |
|Spot|  |
|ExportSessionInfoAsText|  |
|GetDynamicProperties|  |
|SetPlaybackMode|  |
|SetRecordMode|  |
|GetSessionAudioFormat| ☑️ |
|GetSessionSampleRate| ☑️ |
|GetSessionBitDepth| ☑️ |
|GetSessionInterleavedState| ☑ | [Bug Reported](https://duc.avid.com/showthread.php?p=2658177#post2658177) |
|GetSessionTimeCodeRate| ☑️ |
|GetSessionFeetFramesRate| ☑️ |
|GetSessionAudioRatePullSettings| ☑️ |
|GetSessionVideoRatePullSettings| ☑️ |
|GetSessionName| ☑️ |
|GetSessionPath| ☑️ |
|GetSessionStartTime| ☑️ |
|GetSessionLength| ☑️ |
|SetSessionAudioFormat|  |
|SetSessionBitDepth|  |
|SetSessionInterleavedState|  |
|SetSessionTimeCodeRate|  |
|SetSessionFeetFramesRate|  |
|SetSessionAudioRatePullSettings|  |
|SetSessionVideoRatePullSettings|  |
|SetSessionStartTime|  |
|SetSessionLength|  |
|GetPTSLVersion| ☑️ |
|GetPlaybackMode| ☑️ | Bug to report (see class) |
|GetRecordMode| ☑️ |
|GetTransportArmed| ☑️ |
|GetTransportState| ☑️ |
|AuthorizeConnection| ☑️ |
