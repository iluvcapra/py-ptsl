# pt_set.py
#
# This example demonstrates some of the set_* functions of the
# `ptsl.Engine`.

import optparse
from ptsl import open_engine
import ptsl.PTSL_pb2 as pt

import sys

p = optparse.OptionParser()
p.add_option("--cut", action='store_true')
p.add_option("--copy", action='store_true')
p.add_option("--clear", action='store_true')
p.add_option("--paste", action='store_true')

ccc_mods = optparse.OptionGroup(p, "Cut, Copy and Clear Modifiers")
ccc_mods.add_option("--automation", action='store_true')
ccc_mods.add_option("--pan-automation", action='store_true')
ccc_mods.add_option("--plugin-automation", action='store_true')
ccc_mods.add_option("--clip-gain", action='store_true')
ccc_mods.add_option("--clip-fx", action='store_true')
p.add_option_group(ccc_mods)

v_mods = optparse.OptionGroup(p, "Paste Modifiers")
v_mods.add_option("--merge", action='store_true')
v_mods.add_option("--repeat", action='store_true')
v_mods.add_option("--current", action='store_true')
p.add_option_group(v_mods)


(options, _) = p.parse_args()

xcb_modifier = None
if options.automation:
    xcb_modifier = pt.All_Automation
elif options.pan_automation:
    xcb_modifier = pt.Pan_Automation
elif options.plugin_automation:
    xcb_modifier = pt.PlugIn_Automation
elif options.clip_gain:
    xcb_modifier = pt.Clip_Gain
elif options.clip_fx:
    xcb_modifier = pt.Clip_Effects

v_modifier = None
if options.merge:
    v_modifier = pt.Merge
elif options.repeat:
    v_modifier = pt.Repeat_To_Fill_Selection
elif options.current:
    v_modifier = pt.To_Current_Automation_Type


with open_engine(application_name=sys.argv[0], company_name="py-ptsl") as e:
    if options.cut:
        e.cut(special=xcb_modifier)

    elif options.copy:
        e.copy(special=xcb_modifier)

    elif options.paste:
        e.paste(special=v_modifier)

    elif options.clear:
        e.clear(special=xcb_modifier)
