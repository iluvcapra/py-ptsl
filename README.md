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

c = ptsl.client.Client("/Users/jamiehardt/src/ptsl/<your api key>.json")

track_list = c.get_track_list()
```
