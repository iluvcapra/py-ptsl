PTSL Observed Errata
====================

.. currentmodule:: ptsl

:Command:
    SetSessionLength

:Version:
    1

:Observed Behavior:
    When trying to set a session length less than "06:00:00:00", Pro Tools
    returns an Response with an :py:attr:`response_error_json` with a 
    :py:attr:`command_error` value of "PT_InvalidParameter", a string. An error 
    by this name does not exist in the :py:class:`CommandErrorType` 
    enumeration, and it is a string, and not an integer as required by the 
    proto.

:Expected Behavior:
    Pro Tools should return a :py:attr:`response_error_json` with a numeric 
    :py:attr:`command_error` whose value exists in the 
    :py:class:`CommandErrorType` enumeration.

---

:Command:
    SetSessionBitDepth
    SetSessionAudioFormat
    SetSessionLength
    SetSessionAudioPullRateSetting
    SetSessionVideoPullRateSetting
    
:Version:
    1

:Observed Behavior:
    Using these commands does not change the settings in the session setup 
    window. The session must be saved, closed and reopened before the changes
    are visible in Setup.

:Expected Behavior:
    The Session setup window should change its visible settings immediately.


---

:Command:
    PasteSpecial

:Version:
    1

:Observed Behvaior:
    When `PasteSpecial` is used with the `To_Current_Automation_Type`, nothing
    happens.

:Expected Behavior:
    When used in this way, this command should do a Paste to Current.

---

:Command:
    CreateSession

:Version:
    1

:Observed Behavior:
    When this command is used with the path and name of an existing session,
    it will overwrite the existing file on disk without reporting an error.

:Expected Behavior:
    This command should fail with an error if the path and name of a session
    that exists on disk are given. A session exitsing on disk should never be
    overwritten.

---

:Command:
    ExportSessionInfoAsText

:Version:
    1

:Observed Behavior:
    When "ESI_string" is given for the `output_type` in the request, an empty
    response is returned.

:Expected Behavior:
    When the `output_type=ESI_string` parameter-value is given for this 
    command, the command should return a text export as a string with the
    response.
    
:Avid Response:
    PT-297044
    https://duc.avid.com/showthread.php?t=422971

---

:Command:
    GetPlaybackMode

:Version:
    1

:Observed Behavior:
    In the response, `possible_values` is returned as an array of strings and 
    not an array of integer enum values, as per the proto.

:Expected Behavior:
    `possible_values` should return a list of integers corresponding to the
    `PM_PlaybackMode` enum values.

:Avid Response:
    PT-296814
    https://duc.avid.com/showthread.php?p=2659689&posted=1#post2659689

---

:Command:
    GetTrackList

:Version:
    1

:Observed Behavior:
    When there are no tracks in the session, the `track_list` value in the 
    response contains an empty JSON set object `{}` and not an empty JSON list 
    `[]`. This is not the correct type for this variable.

:Expected Behavior:
    Pro Tools should return an empty list value for this value.

---

:Command:
    GetTaskStatus

:Version:
    1

:Observed Behavior:
    When the status of a running task is queried, the response contains an 
    accurate `status` value of `InProgress` but `progress` stays at 0 and never
    progressively increases, it remains at zero through the entire life of the 
    task.

:Expected Behavior:
    The `progress` field should advance and reflect the task's percentage 
    completion.
