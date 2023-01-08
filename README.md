# py-ptsl

Native Python client for the Pro Tools scripting RPC interface

## Work In Progress

This project is in the very early phases of development (almost nothing works). The 
client successfully connects to Pro Tools, will authorize your connection with your
developer key and a few commands are exposed. PRs and issue submissions are welcome
to guide future development!

## Example

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
|GetRecordMode|  |
|GetTransportArmed|  |
|GetTransportState|  |
|AuthorizeConnection| ☑️ |
